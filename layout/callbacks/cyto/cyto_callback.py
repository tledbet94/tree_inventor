from dash import Input, Output, State, ctx
from app_instance import app
import copy
import random
import time
from collections import Counter
from dash.exceptions import PreventUpdate

def single_traversal_with_steps(elements, current_node_id='root', path=None):
    if path is None:
        path = [current_node_id]

    # Reset attributes
    for element in elements:
        data = element['data']
        data['traversed'] = 'False'  # Reset traversed attribute
        data['common'] = 'False'     # Reset common attribute

    # Get the current node's data
    current_node = next((elem for elem in elements if elem['data'].get('id') == current_node_id and 'source' not in elem['data']), None)

    if not current_node:
        # If the current node is not found, terminate the traversal
        return path

    # Find all edges starting from the current node
    edges = [elem for elem in elements if elem['data'].get('source') == current_node_id]

    if not edges:
        # If there are no outgoing edges, it's a terminal node
        return path

    # Include the current node's weight and edges' weights for probability calculation
    total_weight = current_node['data'].get('weight', 0) + sum(edge['data']['weight'] for edge in edges)

    # Create a weighted choice list
    weighted_choices = [(current_node_id, current_node['data'].get('weight', 0))]  # Include the current node itself
    weighted_choices.extend((edge['data']['target'], edge['data']['weight']) for edge in edges)

    # Choose the next node based on the weighted probabilities
    next_node_id = random.choices(
        [choice[0] for choice in weighted_choices],
        weights=[choice[1] for choice in weighted_choices],
        k=1
    )[0]

    path.append(next_node_id)

    # Mark the selected edge if an edge was chosen (not the current node)
    if next_node_id != current_node_id:
        for edge in edges:
            if edge['data']['target'] == next_node_id:
                edge['data']['traversed'] = 'True'

    # If the chosen node is the current node, it is terminal
    if next_node_id == current_node_id:
        return path

    # Recursively traverse the chosen node
    return single_traversal_with_steps(elements, current_node_id=next_node_id, path=path)

def multiple_traversals(elements, num_traversals):
    terminal_nodes = []
    paths = []
    all_visited_nodes = set()
    all_visited_edges = set()
    path_counts = Counter()

    for _ in range(num_traversals):
        path = single_traversal_with_steps(elements)
        paths.append(path)
        terminal_nodes.append(path[-1])  # The last node in the path is the terminal node
        all_visited_nodes.update(path)  # Collect all visited nodes
        path_counts[tuple(path)] += 1    # Count the occurrence of each path

        # Collect visited edges
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            all_visited_edges.add((source, target))

    # Count the occurrences of each terminal node
    terminal_node_counts = Counter(terminal_nodes)
    most_common_node_id, _ = terminal_node_counts.most_common(1)[0]

    # Find the most common path
    most_common_path, _ = path_counts.most_common(1)[0]
    most_common_nodes = set(most_common_path)
    most_common_edges = set(zip(most_common_path[:-1], most_common_path[1:]))

    # Reset attributes and update elements to mark traversed and common nodes and edges
    for element in elements:
        data = element['data']
        data['traversed'] = 'False'  # Reset traversed attribute
        data['common'] = 'False'     # Reset common attribute

        # Mark traversed nodes and edges
        if data['id'] in all_visited_nodes:
            data['traversed'] = 'True'

        # Mark common nodes and edges
        if data['id'] in most_common_nodes:
            data['common'] = 'True'

        if 'source' in data:
            edge_tuple = (data['source'], data['target'])
            if edge_tuple in all_visited_edges:
                data['traversed'] = 'True'

            if edge_tuple in most_common_edges:
                data['common'] = 'True'

    return {
        'paths': paths,
        'terminal_node_counts': terminal_node_counts,
        'most_common_node_id': most_common_node_id
    }

@app.callback(
    [
        Output('cytoscape', 'elements'),
        Output('name-store', 'data'),
        Output('traversal-path', 'data'),
        Output('current-step', 'data'),
        Output('traversal-interval', 'disabled'),
        Output('traversal-output-display', 'className'),
        Output('traversal-output-display', 'children'),
        Output('terminal-node-info', 'data'),
    ],
    [
        Input('edit-input-button', 'n_clicks'),
        Input('remove-button', 'n_clicks'),
        Input('single-traversal-button', 'n_clicks'),
        Input('traversal-interval', 'n_intervals'),
        Input('multiple-traversal-button', 'n_clicks'),
    ],
    [
        State('cytoscape', 'elements'),
        State('cytoscape', 'tapNode'),
        State('edit-input', 'value'),
        State('selected-edit', 'data'),
        State('traversal-path', 'data'),
        State('current-step', 'data'),
        State('traversal-output-display', 'className'),
        State('traversal-output-display', 'children'),
        State('terminal-node-info', 'data'),
        State('algo-slider', 'value')
    ]
)
def modify_cyto(enter_clicks, remove_clicks, single_traversal_clicks, n_intervals,
                multiple_traversal_clicks, elements, tap_node, new_label, edit_selection,
                traversal_path, current_step, output_display_class, display_name, terminal_node_info,
                selected_traversals):

    # Determine which Input triggered the callback
    triggered_id = ctx.triggered_id if ctx.triggered else None

    # Initialize variables
    elements = copy.deepcopy(elements) if elements else []
    traversal_path = traversal_path or []
    current_step = current_step or 0
    current_node_data = None  # Initialize current_node_data

    # Reset 'traversed' and 'common' attributes after copying elements
    for element in elements:
        element['data']['traversed'] = 'False'
        element['data']['common'] = 'False'

    # CSS Classes for Transition
    active_class = 'algo-output-active'
    passive_class = 'algo-output-passive'

    # spinner for multiple traversal
    not_loading = {'textAlign': 'center', 'display': 'block'}
    loading = {'textAlign': 'center', 'display': 'none'}

    ### Rename Function
    if triggered_id == 'edit-input-button' and enter_clicks and tap_node and new_label and edit_selection == 'rename':
        # Update the label of the tapped node
        for element in elements:
            if 'id' in element['data'] and element['data']['id'] == tap_node['data']['id']:
                element['data']['label'] = new_label
                current_node_data = element['data']
                break
        return elements, new_label, traversal_path, current_step, True, output_display_class, display_name, terminal_node_info

    ### Add Function
    if triggered_id == 'edit-input-button' and enter_clicks and tap_node and new_label and edit_selection == 'add':
        # Create a unique ID for the new child node
        new_node_id = f"{tap_node['data']['id']}-child-{enter_clicks}"

        # Collect necessary data from the parent node
        level = int(tap_node['data'].get('level', 1)) + 1
        weight = 100  # Or calculate as needed

        # Add the new child node
        new_node = {
            'data': {
                'id': new_node_id,
                'label': new_label,
                'weight': weight,
                'level': level,
                'Productive?': tap_node['data'].get('Productive?', 'N/A'),
                'Mood Impact': tap_node['data'].get('Mood Impact', 'N/A'),
                'Fun Level': tap_node['data'].get('Fun Level', 'N/A'),
                'traversed': 'False',  # Initialize 'traversed'
                'common': 'False'      # Initialize 'common'
            }
        }

        # Add an edge to link the parent node to the new child node
        new_edge = {
            'data': {
                'id': f"edge-{tap_node['data']['id']}-{new_node_id}",
                'source': tap_node['data']['id'],
                'target': new_node_id,
                'weight': 0,  # Set weight as needed
                'traversed': 'False',  # Initialize 'traversed'
                'common': 'False'      # Initialize 'common'
            }
        }

        # Append the new node and edge to the elements
        elements.extend([new_node, new_edge])

        # Update current_node_data
        current_node_data = new_node['data']

        return elements, new_label, traversal_path, current_step, True, output_display_class, display_name, terminal_node_info

    ### Remove Function
    if triggered_id == 'remove-button' and remove_clicks and tap_node:
        # Remove the tapped node and its connected edges
        elements = [element for element in elements if element['data']['id'] != tap_node['data']['id']
                    and element['data'].get('source') != tap_node['data']['id']
                    and element['data'].get('target') != tap_node['data']['id']]

        return elements, '', traversal_path, current_step, True, output_display_class, display_name, terminal_node_info

    ### Single Traversal Function
    if triggered_id == 'single-traversal-button' and single_traversal_clicks:
        # Deselect all elements
        for element in elements:
            element['selected'] = False

        # Perform single traversal and store the path
        traversal_path = single_traversal_with_steps(elements)
        current_step = 0

        # Enable the interval
        disabled = False

        # Set output display to passive
        output_display_class = passive_class
        display_name = ''

        return elements, '', traversal_path, current_step, disabled, output_display_class, display_name, terminal_node_info

    ### Traversal Interval Function
    if triggered_id == 'traversal-interval' and traversal_path:
        # Reset 'traversed' attribute in element['data']
        for element in elements:
            element['data']['traversed'] = 'False'

        # Select nodes and edges up to the current step
        for i in range(current_step + 1):
            node_id = traversal_path[i]
            for element in elements:
                # Mark nodes as traversed
                if element['data']['id'] == node_id:
                    element['data']['traversed'] = 'True'
                # Mark edges as traversed if they are part of the traversal path
                if i > 0 and element['data'].get('source') == traversal_path[i - 1] and element['data'].get('target') == node_id:
                    element['data']['traversed'] = 'True'

        # Check if traversal is complete
        if current_step >= len(traversal_path) - 1:
            # Disable the interval
            disabled = True

            # Update the traversal-output-display
            terminal_node_id = traversal_path[-1]
            current_node_data = next((elem['data'] for elem in elements if
                                      elem['data']['id'] == terminal_node_id and 'source' not in elem['data']), None)
            output_display_class = active_class
            display_name = current_node_data['label'] if current_node_data else ''
            terminal_node_info = current_node_data

            return (elements, '', traversal_path, current_step, disabled, output_display_class, display_name,
                    terminal_node_info)
        else:
            # Continue traversal
            current_step += 1
            disabled = False
            return elements, '', traversal_path, current_step, disabled, output_display_class, display_name, terminal_node_info

    ### Multiple Traversal Function
    if triggered_id == 'multiple-traversal-button' and multiple_traversal_clicks:
        # Perform multiple traversals
        traversal_results = multiple_traversals(elements, num_traversals=(int(10 ** selected_traversals)))

        # elements are already updated inside multiple_traversals with 'traversed' and 'common' attributes
        # So, you can return them directly

        # Get the most common terminal node
        most_common_node_id = traversal_results['most_common_node_id']
        current_node_data = next(
            (elem['data'] for elem in elements
             if elem['data']['id'] == most_common_node_id and 'source' not in elem['data']),
            None
        )

        # Update the traversal-output-display
        output_display_class = 'algo-output-active'
        display_name = current_node_data['label'] if current_node_data else ''
        terminal_node_info = current_node_data

        # No interval needed for multiple traversals
        disabled = True

        return elements, '', [], 0, disabled, output_display_class, display_name, terminal_node_info

    # Default return if no conditions are met
    raise PreventUpdate
