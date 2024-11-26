from dash import ctx, no_update, Input, Output, State
from app_instance import app
import copy


@app.callback(
    [
        Output('edit-store', 'data'),
        Output('name-store', 'data'),
    ],
    [
        Input('edit-input-button', 'n_clicks'),
        Input('remove-button', 'n_clicks'),
        Input('cytoscape', 'tapNode'),
        Input('cytoscape', 'tapEdge'),
    ],
    [
        State('cytoscape', 'elements'),
        State('edit-input', 'value'),
        State('selected-edit', 'data'),
    ]
)
def modify_elements(enter_clicks, remove_clicks, tap_node, tap_edge, elements, new_label, edit_selection):
    # Copy elements to avoid mutating the original data
    elements = copy.deepcopy(elements) if elements else []
    manual_input_feedback_children = no_update
    selected_element_id = None

    # Determine which Input triggered the callback
    triggered_id = ctx.triggered_id if ctx.triggered else None

    # Handle node/edge selection
    if triggered_id == 'cytoscape' and tap_node:
        selected_element_id = tap_node['data']['id']
    elif triggered_id == 'cytoscape' and tap_edge:
        selected_element_id = tap_edge['data']['id']

    # Rename Function
    if triggered_id == 'edit-input-button' and enter_clicks and tap_node and new_label and edit_selection == 'rename':
        for element in elements:
            if element['data']['id'] == tap_node['data']['id']:
                element['data']['label'] = new_label
                break
        return elements, new_label

    # Add Function
    if triggered_id == 'edit-input-button' and enter_clicks and tap_node and new_label and edit_selection == 'add':
        new_node_id = f"{tap_node['data']['id']}-child-{enter_clicks}"
        level = int(tap_node['data'].get('level', 1)) + 1
        weight = 100  # Adjust as needed

        new_node = {
            'data': {
                'id': new_node_id,
                'label': new_label,
                'weight': weight,
                'level': level,
                'Productive?': tap_node['data'].get('Productive?', 'N/A'),
                'Mood Impact': tap_node['data'].get('Mood Impact', 'N/A'),
                'Fun Level': tap_node['data'].get('Fun Level', 'N/A'),
                'traversed': 'False',
                'common': 'False',
                'invalid_weight': 'False'
            }
        }

        new_edge = {
            'data': {
                'id': f"edge-{tap_node['data']['id']}-{new_node_id}",
                'source': tap_node['data']['id'],
                'target': new_node_id,
                'weight': 0,
                'traversed': 'False',
                'common': 'False',
                'invalid_weight': 'False'
            }
        }

        elements.extend([new_node, new_edge])
        return elements, new_label

    # Remove Function
    if triggered_id == 'remove-button' and remove_clicks and tap_node:
        elements = [element for element in elements if element['data']['id'] != tap_node['data']['id']
                    and element['data'].get('source') != tap_node['data']['id']
                    and element['data'].get('target') != tap_node['data']['id']]
        return elements, ''

    return elements, no_update
