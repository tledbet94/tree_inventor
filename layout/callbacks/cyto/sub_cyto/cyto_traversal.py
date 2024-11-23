from dash import exceptions, no_update, Input, Output, State, ctx
from app_instance import app
import copy

from layout.callbacks.cyto.helper_functions.traversal_helper import (
    build_graph, single_traversal_with_steps, multiple_traversals_batch
)


@app.callback(
    [
        # Outputs for Multiple Traversal
        Output('multiple-interval-store', 'data'),
        Output('multiple-traversal-state', 'data'),
        Output('multiple-traversal-interval', 'disabled'),
        Output('multiple-traversal-progress', 'value'),
        Output('multiple-traversal-progress', 'style'),
        Output('multiple-traversal-progress', 'label'),
        # Outputs for Single Traversal
        Output('single-interval-store', 'data'),
        Output('traversal-path', 'data'),
        Output('current-step', 'data'),
        Output('traversal-interval', 'disabled'),
        # Shared Outputs
        Output('traversal-output-display', 'className'),
        Output('traversal-output-display', 'children'),
        Output('terminal-node-info', 'data'),
        Output('traversal-running', 'data'),
    ],
    [
        Input('multiple-traversal-button', 'n_clicks'),
        Input('multiple-traversal-interval', 'n_intervals'),
        Input('single-traversal-button', 'n_clicks'),
        Input('traversal-interval', 'n_intervals'),
    ],
    [
        State('cytoscape', 'elements'),
        State('multiple-traversal-state', 'data'),
        State('algo-slider', 'value'),
        State('traversal-path', 'data'),
        State('current-step', 'data'),
    ]
)
def handle_traversals(multiple_traversal_clicks, multiple_n_intervals,
                      single_traversal_clicks, single_n_intervals,
                      elements, multiple_state, selected_traversals,
                      traversal_path, current_step):
    # Determine which Input triggered the callback
    triggered_id = ctx.triggered_id if ctx.triggered else None

    # Initialize outputs with no_update
    multiple_interval_store_data = no_update
    multiple_traversal_state_output = no_update
    multiple_traversal_interval_disabled = no_update
    multiple_progress_value = no_update
    multiple_progress_style = no_update
    multiple_progress_label = no_update

    single_interval_store_data = no_update
    traversal_path_output = no_update
    current_step_output = no_update
    traversal_interval_disabled = no_update

    traversal_output_display_class = no_update
    traversal_output_display_children = no_update
    terminal_node_info = no_update
    traversal_running = no_update

    # Copy elements to avoid mutation
    elements = copy.deepcopy(elements)

    if triggered_id == 'multiple-traversal-button':
        # Start Multiple Traversal Logic
        if not multiple_traversal_clicks:
            raise exceptions.PreventUpdate

        # Reset traversed and common attributes
        for element in elements:
            element['data']['traversed'] = 'False'
            element['data']['common'] = 'False'

        total_traversals = int(10 ** selected_traversals)
        traversals_completed = 0
        batch_size = min(10000, total_traversals)

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

        traversal_running = True
        multiple_progress_value = 0
        multiple_progress_style = {'display': 'block', 'width': '100%'}
        multiple_progress_label = '0%'

        multiple_traversal_interval_disabled = False  # Enable the interval

        # Update outputs
        multiple_traversal_state_output = state
        multiple_interval_store_data = elements  # Initial elements
        traversal_output_display_class = 'algo-output-passive'
        traversal_output_display_children = ''
        terminal_node_info = {}

    elif triggered_id == 'multiple-traversal-interval':
        # Update Multiple Traversal Logic
        if not multiple_state or multiple_n_intervals is None:
            raise exceptions.PreventUpdate

        total_traversals = multiple_state.get('total_traversals', 0)
        traversals_completed = multiple_state.get('traversals_completed', 0)
        batch_size = min(10000, total_traversals - traversals_completed)

        if batch_size <= 0:
            # All traversals completed
            multiple_traversal_interval_disabled = True
            traversal_running = False
            multiple_progress_value = 100.0
            multiple_progress_style = {'display': 'none'}
            multiple_progress_label = '100%'

            # Process final results
            all_visited_nodes = set(multiple_state['all_visited_nodes'])
            all_visited_edges = set(tuple(edge) for edge in multiple_state['all_visited_edges'])
            most_common_nodes = set(multiple_state['most_common_path'])
            most_common_edges = set(
                zip(multiple_state['most_common_path'][:-1], multiple_state['most_common_path'][1:]))

            for element in elements:
                data = element['data']
                if data['id'] in all_visited_nodes:
                    data['traversed'] = 'True'
                if data['id'] in most_common_nodes:
                    data['common'] = 'True'
                if 'source' in data:
                    edge_tuple = (data['source'], data['target'])
                    if edge_tuple in all_visited_edges:
                        data['traversed'] = 'True'
                    if edge_tuple in most_common_edges:
                        data['common'] = 'True'

            current_node_data = next(
                (elem['data'] for elem in elements if elem['data']['id'] == multiple_state['most_common_node_id']), None
            )

            traversal_output_display_class = 'algo-output-active'
            traversal_output_display_children = current_node_data['label'] if current_node_data else ''
            terminal_node_info = current_node_data if current_node_data else {}

            # Clear the state
            multiple_traversal_state_output = None
            multiple_interval_store_data = elements
        else:
            # Process batch
            multiple_state = multiple_traversals_batch(multiple_state['graph'], multiple_state['node_weights'],
                                                       batch_size, multiple_state)
            multiple_state['traversals_completed'] += batch_size
            multiple_progress_value = (multiple_state['traversals_completed'] / multiple_state[
                'total_traversals']) * 100.0
            multiple_progress_label = f"{int(multiple_progress_value)}%"
            multiple_progress_style = {'display': 'block', 'width': '100%'}

            # Update elements based on current state
            all_visited_nodes = set(multiple_state['all_visited_nodes'])
            all_visited_edges = set(tuple(edge) for edge in multiple_state['all_visited_edges'])
            most_common_nodes = set(multiple_state['most_common_path'])
            most_common_edges = set(
                zip(multiple_state['most_common_path'][:-1], multiple_state['most_common_path'][1:]))

            for element in elements:
                data = element['data']
                if data['id'] in all_visited_nodes:
                    data['traversed'] = 'True'
                if data['id'] in most_common_nodes:
                    data['common'] = 'True'
                if 'source' in data:
                    edge_tuple = (data['source'], data['target'])
                    if edge_tuple in all_visited_edges:
                        data['traversed'] = 'True'
                    if edge_tuple in most_common_edges:
                        data['common'] = 'True'

            traversal_running = True
            multiple_traversal_interval_disabled = False
            multiple_traversal_state_output = multiple_state
            multiple_interval_store_data = elements

    elif triggered_id == 'single-traversal-button':
        # Start Single Traversal Logic
        if not single_traversal_clicks:
            raise exceptions.PreventUpdate

        # Reset traversed and common attributes
        elements_to_use = copy.deepcopy(elements)
        for element in elements_to_use:
            element['data']['traversed'] = 'False'
            element['data']['common'] = 'False'

        # Build the graph
        graph, node_weights = build_graph(elements_to_use)

        # Perform single traversal
        traversal_path = single_traversal_with_steps(graph, node_weights)
        current_step = 0
        traversal_running = True

        # Update outputs
        traversal_path_output = traversal_path
        current_step_output = current_step
        traversal_interval_disabled = False
        traversal_output_display_class = 'algo-output-passive'
        traversal_output_display_children = ''
        terminal_node_info = {}
        single_interval_store_data = elements_to_use

    elif triggered_id == 'traversal-interval':
        # Update Single Traversal Logic
        if not traversal_path or single_n_intervals is None:
            raise exceptions.PreventUpdate

        # Use elements from single_interval_store_data if available
        elements_to_use = elements

        elements_to_use = copy.deepcopy(elements_to_use)

        # Reset traversed and common attributes at the start
        if current_step == 0:
            for element in elements_to_use:
                element['data']['traversed'] = 'False'
                element['data']['common'] = 'False'

        # Update elements based on traversal_path
        for i in range(current_step + 1):
            node_id = traversal_path[i]
            for element in elements_to_use:
                if element['data']['id'] == node_id:
                    element['data']['traversed'] = 'True'
                if i > 0 and element['data'].get('source') == traversal_path[i - 1] and element['data'].get(
                        'target') == node_id:
                    element['data']['traversed'] = 'True'

        # Check if traversal is complete
        if current_step >= len(traversal_path) - 1:
            traversal_interval_disabled = True
            terminal_node_id = traversal_path[-1]
            current_node_data = next(
                (elem['data'] for elem in elements_to_use if elem['data']['id'] == terminal_node_id), None)
            traversal_running = False
            traversal_output_display_class = 'algo-output-active'
            traversal_output_display_children = current_node_data['label'] if current_node_data else ''
            terminal_node_info = current_node_data if current_node_data else {}
            single_interval_store_data = elements_to_use
            current_step_output = current_step
        else:
            current_step += 1
            traversal_interval_disabled = False
            traversal_running = True
            single_interval_store_data = elements_to_use
            current_step_output = current_step

    else:
        # No action needed
        raise exceptions.PreventUpdate

    # Return all outputs
    return (
        # Multiple Traversal Outputs
        multiple_interval_store_data,
        multiple_traversal_state_output,
        multiple_traversal_interval_disabled,
        multiple_progress_value,
        multiple_progress_style,
        multiple_progress_label,
        # Single Traversal Outputs
        single_interval_store_data,
        traversal_path_output,
        current_step_output,
        traversal_interval_disabled,
        # Shared Outputs
        traversal_output_display_class,
        traversal_output_display_children,
        terminal_node_info,
        traversal_running,
    )
