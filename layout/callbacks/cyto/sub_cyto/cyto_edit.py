from dash import callback, ctx, Input, Output, State
import copy


@callback(
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

    # remove function
    if triggered_id == 'remove-button' and remove_clicks and tap_node:
        # Root node cannot be deleted
        if tap_node['data']['id'] == 'root':
            return [elements]
        else:
            parent_id = ''
            # Find parent for redistributing weights
            for element in elements:
                if 'source' in element['data'] and element['data']['target'] == tap_node['data']['id']:
                    parent_id = element['data']['source']
                    break  # Parent found

            # Function to redistribute weights after deletion
            def redistribute_weights(parent_id):
                # Find the parent node
                parent_element = next((e for e in elements if e['data'].get('id') == parent_id), None)
                if not parent_element:
                    # Parent not found, nothing to redistribute
                    return elements

                parent_weight = float(parent_element['data'].get('weight', 0))

                # Find remaining child edges
                remaining_child_edges = [
                    e for e in elements if 'source' in e['data'] and e['data']['source'] == parent_id
                ]

                # Total weight available for child edges
                total_weight_for_edges = 100 - parent_weight

                if not remaining_child_edges:
                    # No remaining child edges, set parent weight to 100%
                    parent_element['data']['weight'] = 100.0
                else:
                    # Adjust weights proportionally among parent and child edges
                    total_current_weight = parent_weight + sum(
                        float(e['data'].get('weight', 0)) for e in remaining_child_edges
                    )

                    # Update parent weight
                    parent_element['data']['weight'] = round((parent_weight / total_current_weight) * 100, 2)

                    # Update child edges' weights
                    for edge in remaining_child_edges:
                        edge_weight = float(edge['data'].get('weight', 0))
                        new_weight = round((edge_weight / total_current_weight) * 100, 2)
                        edge['data']['weight'] = new_weight

                return elements

            # Function to get all descendants of a node
            def get_descendants(node_id, elements):
                descendants = set()
                nodes_to_visit = [node_id]
                while nodes_to_visit:
                    current_node_id = nodes_to_visit.pop()
                    for e in elements:
                        if 'source' in e['data'] and e['data']['source'] == current_node_id:
                            child_node_id = e['data']['target']
                            if child_node_id not in descendants:
                                descendants.add(child_node_id)
                                nodes_to_visit.append(child_node_id)
                return descendants

            # Get all descendants of the node to be removed
            descendants = get_descendants(tap_node['data']['id'], elements)
            nodes_to_remove = descendants.union({tap_node['data']['id']})

            # Remove nodes and associated edges
            elements = [
                e for e in elements
                if e['data'].get('id') not in nodes_to_remove and
                   not ('source' in e['data'] and (
                               e['data']['source'] in nodes_to_remove or e['data']['target'] in nodes_to_remove))
            ]

            # Redistribute weights
            elements = redistribute_weights(parent_id)

            return [elements]  # Wrap in a list

    # Else, return elements unchanged
    return [elements]
