from dash import Input, Output, State, ctx, dcc, dash
from app_instance import app
import copy
from collections import Counter

from layout.callbacks.cyto.helper_functions.traversal_helper import \
    build_graph, single_traversal_with_steps, multiple_traversals_batch
from layout.callbacks.cyto.helper_functions.weight_helper import \
    get_system_info, auto_balance_system, proximity_to_100


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
        Output('traversal-running', 'data'),
        # Outputs for weight adjustment
        Output('manual-input-feedback', 'children'),
        Output('system-weights-progress', 'value'),
        Output('system-weights-progress', 'style'),
        Output('system-weights-progress', 'label'),
    ],
    [
        Input('edit-input-button', 'n_clicks'),
        Input('remove-button', 'n_clicks'),
        Input('single-traversal-button', 'n_clicks'),
        Input('traversal-interval', 'n_intervals'),
        Input('multiple-traversal-button', 'n_clicks'),
        Input('multiple-traversal-interval', 'n_intervals'),
        Input('weights-input-button', 'n_clicks'),
        Input('manual-button', 'n_clicks'),
        Input('auto-button', 'n_clicks'),
        Input('active-button-store', 'data'),
        Input('cytoscape', 'tapNode'),
        Input('cytoscape', 'tapEdge'),
    ],
    [
        State('cytoscape', 'elements'),
        State('edit-input', 'value'),
        State('selected-edit', 'data'),
        State('traversal-path', 'data'),
        State('current-step', 'data'),
        State('traversal-output-display', 'className'),
        State('traversal-output-display', 'children'),
        State('terminal-node-info', 'data'),
        State('algo-slider', 'value'),
        State('multiple-traversal-state', 'data'),
        State('traversal-running', 'data'),
        # States for weight adjustment
        State('weights-input', 'value'),
        State('manual-button', 'className'),
        State('auto-button', 'className'),
    ]
)
def modify_cyto(enter_clicks, remove_clicks, single_traversal_clicks, n_intervals,
                multiple_traversal_clicks, multiple_traversal_n_intervals,
                weights_enter_clicks, manual_button_clicks, auto_button_clicks, selected_panel,
                tap_node, tap_edge, elements, new_label, edit_selection,
                traversal_path, current_step, output_display_class, display_name, terminal_node_info,
                selected_traversals, multiple_traversal_state, traversal_running,
                weights_input_value, manual_button_classname, auto_button_classname):
    # Determine which Input triggered the callback
    triggered_id = ctx.triggered_id if ctx.triggered else None

    # Initialize variables
    elements = copy.deepcopy(elements) if elements else []
    traversal_path = traversal_path or []
    current_step = current_step or 0
    current_node_data = None  # Initialize current_node_data
    progress_value = dash.no_update
    progress_style = dash.no_update
    progress_label = dash.no_update
    traversal_running = traversal_running or False  # Initialize traversal_running
    manual_input_feedback_children = dash.no_update
    system_weights_progress_value = dash.no_update
    system_weights_progress_style = dash.no_update
    system_weights_progress_label = dash.no_update

    # Determine which property triggered the callback
    triggered_props = [p['prop_id'] for p in ctx.triggered]

    # Initialize selected_element_id and selected_element_type
    selected_element_id = None
    selected_element_type = None
    selected_element = None

    # Check if a node or edge was clicked
    if 'cytoscape.tapNode' in triggered_props and tap_node:
        # Reset last_clicked for all elements
        for element in elements:
            element['data']['last_clicked'] = False

        selected_element_id = tap_node['data']['id']
        selected_element_type = 'node'

        # Set last_clicked = True for the tapped node
        for element in elements:
            if element['data']['id'] == selected_element_id:
                element['data']['last_clicked'] = True
                selected_element = element
                break

    elif 'cytoscape.tapEdge' in triggered_props and tap_edge:
        # Reset last_clicked for all elements
        for element in elements:
            element['data']['last_clicked'] = False

        selected_element_id = tap_edge['data']['id']
        selected_element_type = 'edge'

        # Set last_clicked = True for the tapped edge
        for element in elements:
            if element['data']['id'] == selected_element_id:
                element['data']['last_clicked'] = True
                selected_element = element
                break
    else:
        # If no node or edge was clicked, keep last_clicked as it is
        # Find the element that has last_clicked == True
        for element in elements:
            if element['data'].get('last_clicked'):
                selected_element_id = element['data']['id']
                if 'source' in element['data'] and 'target' in element['data']:
                    selected_element_type = 'edge'
                else:
                    selected_element_type = 'node'
                selected_element = element
                break

    # Clear the last_clicked attribute for all elements
    selected_element_id = None
    selected_element = None
    # Determine which property triggered the callback
    triggered_props = [p['prop_id'] for p in ctx.triggered]
    if 'cytoscape.tapEdge' in triggered_props and tap_edge:
        selected_element_id = tap_edge['data']['id']
        selected_element_type = 'edge'
    elif 'cytoscape.tapNode' in triggered_props and tap_node:
        selected_element_id = tap_node['data']['id']
        selected_element_type = 'node'

    if selected_element_id:
        for element in elements:
            if element['data']['id'] == selected_element_id:
                element['data']['last_clicked'] = 'True'
                break

    # CSS Classes for Transition
    active_class = 'algo-output-active'
    passive_class = 'algo-output-passive'

    # Wipe the common and traversed styles if traversal was run in algo section
    if selected_panel != 'algo':
        for element in elements:
            element['data']['traversed'] = 'False'
            element['data']['common'] = 'False'

    ### Weight Adjustment Function
    if triggered_id == 'weights-input-button' and weights_enter_clicks and weights_input_value is not None:
        # Determine the mode
        if 'active' in manual_button_classname:
            mode = 'manual'
        elif 'active' in auto_button_classname:
            mode = 'automatic'
        else:
            mode = 'manual'  # Default to manual mode

        # Convert input value to float
        try:
            entered_weight = float(weights_input_value)
        except ValueError:
            entered_weight = 0.0  # Handle invalid input

        # Clamp entered_weight between 0 and 100
        entered_weight = max(0.0, min(entered_weight, 100.0))

        # Proceed only if a selected element is available
        selected_element, element_type, system_elements, system_weight, message = get_system_info(elements)

        if not selected_element:
            # No element selected, provide feedback
            manual_input_feedback_children = "No element selected. Please select a node or edge."
            return (
                elements, dash.no_update, traversal_path, current_step, True, output_display_class, display_name,
                terminal_node_info, True, multiple_traversal_state, dash.no_update, dash.no_update, dash.no_update,
                traversal_running, manual_input_feedback_children, system_weights_progress_value,
                system_weights_progress_style, system_weights_progress_label
            )

        # Update the weight of the selected element
        selected_element['data']['weight'] = entered_weight

        # Recalculate system weight
        _, _, system_elements, system_weight, message = get_system_info(elements)

        if mode == 'manual':
            # Manual mode: Validate the system and provide feedback
            # Do not adjust any weights automatically
            feedback_message = message

            # Update progress bar
            progress_value = proximity_to_100(system_weight)
            progress_label = ''
            if system_weight != 100:
                progress_style = {'display': 'block'}
                traversal_running = True
            else:
                progress_style = {'display': 'none'}
                traversal_running = False
            manual_input_feedback_children = feedback_message

            return (
                elements, dash.no_update, traversal_path, current_step, True, output_display_class, display_name,
                terminal_node_info, True, multiple_traversal_state,
                progress_value, progress_style, progress_label,
                traversal_running, manual_input_feedback_children,
                progress_value, progress_style, progress_label
            )

        elif mode == 'automatic':
            # Automatic mode: Adjust the weights to maintain 100% total
            elements, feedback_message = auto_balance_system(elements)

            # Recalculate system weight
            _, _, _, system_weight, _ = get_system_info(elements)

            # Update progress bar
            progress_value = 0
            progress_label = ''
            progress_style = {'display': 'none'}

            manual_input_feedback_children = feedback_message

            return (
                elements, dash.no_update, traversal_path, current_step, True, output_display_class, display_name,
                terminal_node_info, True, multiple_traversal_state,
                progress_value, progress_style, progress_label,
                traversal_running, manual_input_feedback_children,
                progress_value, progress_style, progress_label
            )

    ### Rename Function
    if triggered_id == 'edit-input-button' and enter_clicks and tap_node and new_label and edit_selection == 'rename':
        # Update the label of the tapped node
        for element in elements:
            if 'id' in element['data'] and element['data']['id'] == tap_node['data']['id']:
                element['data']['label'] = new_label
                current_node_data = element['data']
                break
        # Hide the progress bar
        return elements, new_label, traversal_path, current_step, True, output_display_class, display_name, terminal_node_info, True, multiple_traversal_state, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

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
                'common': 'False',  # Initialize 'common'
                'invalid_weight': 'False'  # Initialize 'invalid_weight'
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
                'common': 'False',  # Initialize 'common'
                'invalid_weight': 'False'  # Initialize 'invalid_weight'
            }
        }

        # Append the new node and edge to the elements
        elements.extend([new_node, new_edge])

        # Update current_node_data
        current_node_data = new_node['data']

        # Hide the progress bar
        return elements, new_label, traversal_path, current_step, True, output_display_class, display_name, terminal_node_info, True, multiple_traversal_state, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

    ### Remove Function
    if triggered_id == 'remove-button' and remove_clicks and tap_node:
        # Remove the tapped node and its connected edges
        elements = [element for element in elements if element['data']['id'] != tap_node['data']['id']
                    and element['data'].get('source') != tap_node['data']['id']
                    and element['data'].get('target') != tap_node['data']['id']]

        # Hide the progress bar
        return elements, '', traversal_path, current_step, True, output_display_class, display_name, terminal_node_info, True, multiple_traversal_state, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

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

        # Set traversal_running to True
        traversal_running = True

        # Hide the progress bar
        return elements, '', traversal_path, current_step, disabled, output_display_class, display_name, {}, True, {}, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

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
                if i > 0 and element['data'].get('source') == traversal_path[i - 1] and element['data'].get(
                        'target') == node_id:
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

            # Set traversal_running to False
            traversal_running = False

            # Hide the progress bar
            return (elements, '', traversal_path, current_step, disabled, output_display_class, display_name,
                    terminal_node_info, True, {}, progress_value, progress_style, progress_label, traversal_running,
                    manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style,
                    system_weights_progress_label)
        else:
            # Continue traversal
            current_step += 1
            disabled = False
            # traversal_running remains True
            return elements, '', traversal_path, current_step, disabled, output_display_class, display_name, {}, True, {}, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

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
        progress_value = 0
        progress_style = {'display': 'block', 'width': '100%'}
        progress_label = '0%'

        # Set traversal_running to True
        traversal_running = True

        return elements, '', [], 0, True, output_display_class, display_name, {}, disabled, state, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

    ### Multiple Traversal Interval Function
    if triggered_id == 'multiple-traversal-interval':
        if multiple_traversal_state is None:
            # No state, nothing to do
            disabled = True
            traversal_running = False
            return elements, '', [], 0, True, output_display_class, display_name, {}, disabled, None, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

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
            traversal_running = False

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

            return elements, '', [], 0, True, output_display_class, display_name, terminal_node_info, disabled, None, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

        else:
            # Process a batch of traversals
            state = multiple_traversals_batch(graph, node_weights, batch_size, state)

            # Update traversals_completed
            state['traversals_completed'] += batch_size

            # Compute progress value
            progress_value = (state['traversals_completed'] / state['total_traversals']) * 100.0
            progress_value = int(progress_value)
            progress_label = f"{progress_value}%"

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
            traversal_running = True

            # For performance, we can limit updates to elements periodically
            return elements, '', [], 0, True, output_display_class, display_name, {}, disabled, state, progress_value, progress_style, progress_label, traversal_running, manual_input_feedback_children, system_weights_progress_value, system_weights_progress_style, system_weights_progress_label

    # Default return if no conditions are met
    return (
        elements, dash.no_update, traversal_path, current_step, True, output_display_class, display_name,
        terminal_node_info, True, multiple_traversal_state, dash.no_update, dash.no_update, dash.no_update,
        traversal_running, manual_input_feedback_children, system_weights_progress_value,
        system_weights_progress_style, system_weights_progress_label
    )
