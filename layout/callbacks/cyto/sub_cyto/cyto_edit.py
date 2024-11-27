from dash import ctx, Input, Output, State
from app_instance import app
import copy


@app.callback(
    [
        Output('edit-store', 'data')
    ],
    [
        Input('edit-input-button', 'n_clicks'),
        Input('remove-button', 'n_clicks'),
        Input('cytoscape', 'tapNode')
    ],
    [
        State('cytoscape', 'elements'),
        State('edit-input', 'value'),
        State('selected-edit', 'data'),
    ]
)
def modify_elements(enter_clicks, remove_clicks, tap_node, elements, new_label, edit_selection):
    # Working with copied elements is best practice
    elements = copy.deepcopy(elements) if elements else []

    # Identify which button was pressed
    triggered_id = ctx.triggered_id if ctx.triggered else None

    # Rename Function
    if (triggered_id == 'edit-input-button' and enter_clicks and tap_node and
            new_label and edit_selection == 'rename'):
        for element in elements:
            if element['data']['id'] == tap_node['data']['id']:
                element['data']['label'] = new_label
                break
        return [elements]  # Wrap in a list

    # Add Function
    if (triggered_id == 'edit-input-button' and enter_clicks and tap_node and
            new_label and edit_selection == 'add'):
        new_node_id = f"{tap_node['data']['id']}-child-{enter_clicks}"
        level = int(tap_node['data'].get('level', 1)) + 1
        weight = 100  # Adjust as needed

        # Create a new node with inherited and default fields
        new_node = {
            'data': {
                'id': new_node_id,
                'label': new_label,
                'weight': weight,
                'level': level,
                'traversed': 'False',
                'common': 'False',
                'invalid_weight': 'False',
                'last_clicked': False,
                'custom1': {
                    'field_name': tap_node['data']['custom1']['field_name'],
                    'field_value': '-'
                },
                'custom2': {
                    'field_name': tap_node['data']['custom2']['field_name'],
                    'field_value': '-'
                },
                'custom3': {
                    'field_name': tap_node['data']['custom3']['field_name'],
                    'field_value': '-'
                },
            }
        }

        # Add the new node and edge to elements
        elements.append(new_node)
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
        elements.append(new_edge)

        return [elements]  # Wrap in a list

    # Remove Function
    if triggered_id == 'remove-button' and remove_clicks and tap_node:
        # Root node cannot be deleted
        if tap_node['data']['id'] == 'root':
            return [elements]
        else:
            # Find children of the node to be removed
            children = []
            for element in elements:
                if 'source' in element['data']:
                    if element['data']['source'] == tap_node['data']['id']:
                        children.append(element['data']['id'])
                        children.append(element['data']['target'])
            if len(children) == 0:
                # Remove the leaf node
                elements = [element for element in elements if element['data']['id'] != tap_node['data']['id']]
                return [elements]  # Wrap in a list
            else:
                # Remove the branch and its children
                new_elements = []
                for element in elements:
                    if element['data']['id'] != tap_node['data']['id'] and element['data']['id'] not in children:
                        new_elements.append(element)
                return [new_elements]  # Wrap in a list

    return [elements]  # Wrap in a list
