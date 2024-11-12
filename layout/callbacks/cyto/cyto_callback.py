from dash import Input, Output, State, ctx, dcc
from app_instance import app
import copy
import random
from collections import Counter
from dash.exceptions import PreventUpdate

def build_graph(elements):
    graph = {}
    node_weights = {}
    for element in elements:
        data = element['data']
        if 'source' in data and 'target' in data:
            # It's an edge
            source = data['source']
            target = data['target']
            weight = data.get('weight', 0)
            if source not in graph:
                graph[source] = []
            graph[source].append((target, weight))
        elif 'id' in data and 'source' not in data and 'target' not in data:
            # It's a node
            node_id = data['id']
            weight = data.get('weight', 0)
            node_weights[node_id] = weight
            if node_id not in graph:
                graph[node_id] = []

    return graph, node_weights

def single_traversal_with_steps(graph, node_weights, current_node_id='root', path=None):
    if path is None:
        path = [current_node_id]

    # Get the current node's weight
    current_node_weight = node_weights.get(current_node_id, 0)

    # Get the edges from the current node
    edges = graph.get(current_node_id, [])

    if not edges:
        # If there are no outgoing edges, it's a terminal node
        return path

    # Include the current node's weight and edges' weights for probability calculation
    weighted_choices = [(current_node_id, current_node_weight)]  # Include the current node itself
    weighted_choices.extend(edges)

    # Choose the next node based on the weighted probabilities
    next_node_id = random.choices(
        [choice[0] for choice in weighted_choices],
        weights=[choice[1] for choice in weighted_choices],
        k=1
    )[0]

    path.append(next_node_id)

    # If the chosen node is the current node, it is terminal
    if next_node_id == current_node_id:
        return path

    # Recursively traverse the chosen node
    return single_traversal_with_steps(graph, node_weights, current_node_id=next_node_id, path=path)

def multiple_traversals_batch(graph, node_weights, batch_size, state=None):
    if state is None:
        state = {
            'terminal_node_counts': Counter(),
            'path_counts': Counter(),
            'most_common_node_id': None,
            'most_common_path': [],
            'all_visited_nodes': set(),
            'all_visited_edges': set(),
        }
    else:
        # Convert lists back to sets and Counters
        state['all_visited_nodes'] = set(state.get('all_visited_nodes', []))
        state['all_visited_edges'] = set(tuple(edge) for edge in state.get('all_visited_edges', []))
        state['path_counts'] = Counter(state.get('path_counts', {}))
        state['terminal_node_counts'] = Counter(state.get('terminal_node_counts', {}))

    for _ in range(batch_size):
        path = single_traversal_with_steps(graph, node_weights)
        terminal_node = path[-1]
        state['terminal_node_counts'][terminal_node] += 1
        path_tuple = tuple(path)
        state['path_counts'][path_tuple] += 1

        # Collect visited nodes and edges
        state['all_visited_nodes'].update(path)
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            state['all_visited_edges'].add((source, target))

    # Update the most common node
    most_common_node = state['terminal_node_counts'].most_common(1)
    if most_common_node:
        state['most_common_node_id'] = most_common_node[0][0]
    else:
        state['most_common_node_id'] = None

    # Find the most common path
    most_common_path = state['path_counts'].most_common(1)
    if most_common_path:
        state['most_common_path'] = most_common_path[0][0]
    else:
        state['most_common_path'] = []

    # Convert sets back to lists for JSON serialization
    state['all_visited_nodes'] = list(state['all_visited_nodes'])
    state['all_visited_edges'] = [list(edge) for edge in state['all_visited_edges']]
    state['path_counts'] = {str(k): v for k, v in state['path_counts'].items()}
    state['terminal_node_counts'] = dict(state['terminal_node_counts'])

    return state

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
        Output('multiple-traversal-interval', 'disabled'),
        Output('multiple-traversal-state', 'data'),
        Output('multiple-traversal-progress', 'value'),
        Output('multiple-traversal-progress', 'style'),
        Output('multiple-traversal-progress', 'label'),
    ],
    [
        Input('edit-input-button', 'n_clicks'),
        Input('remove-button', 'n_clicks'),
        Input('single-traversal-button', 'n_clicks'),
        Input('traversal-interval', 'n_intervals'),
        Input('multiple-traversal-button', 'n_clicks'),
        Input('multiple-traversal-interval', 'n_intervals'),
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
        State('algo-slider', 'value'),
        State('multiple-traversal-state', 'data'),
    ]
)
def modify_cyto(enter_clicks, remove_clicks, single_traversal_clicks, n_intervals,
                multiple_traversal_clicks, multiple_traversal_n_intervals,
                elements, tap_node, new_label, edit_selection,
                traversal_path, current_step, output_display_class, display_name, terminal_node_info,
                selected_traversals, multiple_traversal_state):

    # Determine which Input triggered the callback
    triggered_id = ctx.triggered_id if ctx.triggered else None

    # Initialize variables
    elements = copy.deepcopy(elements) if elements else []
    traversal_path = traversal_path or []
    current_step = current_step or 0
    current_node_data = None  # Initialize current_node_data
    progress_value = 0.0
    progress_style = {'display': 'none'}
    progress_label = ''

    # CSS Classes for Transition
    active_class = 'algo-output-active'
    passive_class = 'algo-output-passive'

    ### Rename Function
    if triggered_id == 'edit-input-button' and enter_clicks and tap_node and new_label and edit_selection == 'rename':
        # Update the label of the tapped node
        for element in elements:
            if 'id' in element['data'] and element['data']['id'] == tap_node['data']['id']:
                element['data']['label'] = new_label
                current_node_data = element['data']
                break
        # Hide the progress bar
        return elements, new_label, traversal_path, current_step, True, output_display_class, display_name, terminal_node_info, True, multiple_traversal_state, progress_value, progress_style, progress_label

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

        # Hide the progress bar
        return elements, new_label, traversal_path, current_step, True, output_display_class, display_name, terminal_node_info, True, multiple_traversal_state, progress_value, progress_style, progress_label

    ### Remove Function
    if triggered_id == 'remove-button' and remove_clicks and tap_node:
        # Remove the tapped node and its connected edges
        elements = [element for element in elements if element['data']['id'] != tap_node['data']['id']
                    and element['data'].get('source') != tap_node['data']['id']
                    and element['data'].get('target') != tap_node['data']['id']]

        # Hide the progress bar
        return elements, '', traversal_path, current_step, True, output_display_class, display_name, terminal_node_info, True, multiple_traversal_state, progress_value, progress_style, progress_label

    ### Single Traversal Function
    if triggered_id == 'single-traversal-button' and single_traversal_clicks:
        # Deselect all elements and reset styles
        for element in elements:
            element['selected'] = False
            element['data']['traversed'] = 'False'
            element['data']['common'] = 'False'

        # Build the graph for single traversal
        graph, node_weights = build_graph(elements)

        # Perform single traversal and store the path
        traversal_path = single_traversal_with_steps(graph, node_weights)
        current_step = 0

        # Enable the interval
        disabled = False

        # Set output display to passive
        output_display_class = passive_class
        display_name = ''

        # Hide the progress bar
        return elements, '', traversal_path, current_step, disabled, output_display_class, display_name, {}, True, {}, progress_value, progress_style, progress_label

    ### Traversal Interval Function
    if triggered_id == 'traversal-interval' and traversal_path:
        # Reset 'traversed' and 'common' attributes in element['data'] at the start of traversal
        if current_step == 0:
            for element in elements:
                element['data']['traversed'] = 'False'
                element['data']['common'] = 'False'

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

            # Hide the progress bar
            return (elements, '', traversal_path, current_step, disabled, output_display_class, display_name,
                    terminal_node_info, True, {}, progress_value, progress_style, progress_label)
        else:
            # Continue traversal
            current_step += 1
            disabled = False
            return elements, '', traversal_path, current_step, disabled, output_display_class, display_name, {}, True, {}, progress_value, progress_style, progress_label

    ### Multiple Traversal Function (Start)
    if triggered_id == 'multiple-traversal-button' and multiple_traversal_clicks:
        # Reset styles before starting traversal
        for element in elements:
            element['data']['traversed'] = 'False'
            element['data']['common'] = 'False'

        # Initialize traversal state
        total_traversals = int(10 ** selected_traversals)
        traversals_completed = 0
        batch_size = min(10000, total_traversals)  # Adjust batch size as needed

        # Build the graph
        graph, node_weights = build_graph(elements)

        # Initialize state
        state = {
            'graph': graph,
            'node_weights': node_weights,
            'total_traversals': total_traversals,
            'traversals_completed': traversals_completed,
            'terminal_node_counts': {},
            'path_counts': {},
            'most_common_node_id': None,
            'most_common_path': [],
            'all_visited_nodes': [],
            'all_visited_edges': [],
        }

        # Enable the interval
        disabled = False

        # Initialize progress bar
        progress_value = 0.0
        progress_style = {'display': 'block', 'width': '100%'}
        progress_label = '0%'

        return elements, '', [], 0, True, output_display_class, display_name, {}, disabled, state, progress_value, progress_style, progress_label

    ### Multiple Traversal Interval Function
    if triggered_id == 'multiple-traversal-interval':
        if multiple_traversal_state is None:
            # No state, nothing to do
            disabled = True
            return elements, '', [], 0, True, output_display_class, display_name, {}, disabled, None, progress_value, progress_style, progress_label

        # Read the state
        state = multiple_traversal_state

        total_traversals = state.get('total_traversals', 0)
        traversals_completed = state.get('traversals_completed', 0)
        batch_size = min(10000, total_traversals - traversals_completed)  # Adjust batch size as needed

        graph = state['graph']
        node_weights = state['node_weights']

        if batch_size <= 0:
            # All traversals completed
            disabled = True

            # Set progress bar value to 100, hide progress bar
            progress_value = 100.0
            progress_style = {'display': 'none'}
            progress_label = '100%'

            # Update elements based on state
            # Convert lists back to sets and Counters
            all_visited_nodes = set(state['all_visited_nodes'])
            all_visited_edges = set(tuple(edge) for edge in state['all_visited_edges'])
            path_counts = Counter({eval(k): v for k, v in state['path_counts'].items()})
            terminal_node_counts = Counter(state['terminal_node_counts'])
            most_common_node_id = state['most_common_node_id']
            most_common_path = state['most_common_path']

            most_common_nodes = set(most_common_path)
            most_common_edges = set(zip(most_common_path[:-1], most_common_path[1:]))

            # Reset attributes and update elements to mark traversed and common nodes and edges
            for element in elements:
                data = element['data']
                # Styles remain after traversal completion
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

            # Update the traversal-output-display
            current_node_data = next(
                (elem['data'] for elem in elements
                 if elem['data']['id'] == most_common_node_id and 'source' not in elem['data']),
                None
            )

            # Update the traversal-output-display
            output_display_class = 'algo-output-active'
            display_name = current_node_data['label'] if current_node_data else ''
            terminal_node_info = current_node_data

            # Remove 'graph' and 'node_weights' from state before storing
            state.pop('graph', None)
            state.pop('node_weights', None)

            return elements, '', [], 0, True, output_display_class, display_name, terminal_node_info, disabled, None, progress_value, progress_style, progress_label

        else:
            # Process a batch of traversals
            state = multiple_traversals_batch(graph, node_weights, batch_size, state)

            # Update traversals_completed
            state['traversals_completed'] += batch_size

            # Compute progress value
            progress_value = (state['traversals_completed'] / state['total_traversals']) * 100.0
            progress_label = f"{progress_value:.1f}%"

            # Keep the progress bar visible
            progress_style = {'display': 'block', 'width': '100%'}

            # Update elements based on the current state
            # Convert lists back to sets
            all_visited_nodes = set(state['all_visited_nodes'])
            all_visited_edges = set(tuple(edge) for edge in state['all_visited_edges'])
            most_common_nodes = set(state['most_common_path'])
            most_common_edges = set(zip(state['most_common_path'][:-1], state['most_common_path'][1:]))

            # Reset attributes and update elements to mark traversed and common nodes and edges
            for element in elements:
                data = element['data']
                # Only update traversed and common if they are not already True
                if data['traversed'] != 'True' and data['id'] in all_visited_nodes:
                    data['traversed'] = 'True'

                if data['common'] != 'True' and data['id'] in most_common_nodes:
                    data['common'] = 'True'

                if 'source' in data:
                    edge_tuple = (data['source'], data['target'])
                    if data['traversed'] != 'True' and edge_tuple in all_visited_edges:
                        data['traversed'] = 'True'

                    if data['common'] != 'True' and edge_tuple in most_common_edges:
                        data['common'] = 'True'

            # Keep the interval enabled
            disabled = False

            # For performance, we can limit updates to elements periodically
            return elements, '', [], 0, True, output_display_class, display_name, {}, disabled, state, progress_value, progress_style, progress_label

    # Default return if no conditions are met
    raise PreventUpdate
