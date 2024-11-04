from dash import Input, Output, State
from app_instance import app


# Callback to update the label of the tapped node
@app.callback(
    [Output('cytoscape', 'elements'),
     Output('name-store', 'data')],
    [Input('edit-input-button', 'n_clicks'),
     Input('remove-button', 'n_clicks')],
    [State('cytoscape', 'elements'),
     State('cytoscape', 'tapNode'),
     State('edit-input', 'value'),
     State('selected-edit', 'data'),
     State('name-store', 'data')]
)
def modify_cyto(enter_clicks, remove_clicks, elements, tap_node, new_label, edit_selection, name_store):
    enter_clicks = enter_clicks or 0
    remove_clicks = remove_clicks or 0

    ### Rename function
    if enter_clicks > 0 and tap_node and new_label and edit_selection == 'rename':
        # Find the tapped node in the elements and update its label
        for element in elements:
            if 'id' in element['data'] and element['data']['id'] == tap_node['data']['id']:
                element['data']['label'] = new_label
                break
        return elements, new_label

    ### Add function
    if enter_clicks > 0 and tap_node and new_label and edit_selection == 'add':
        # Create a unique ID for the new child node
        new_node_id = f"{tap_node['data']['id']}-child-{enter_clicks}"

        name = str(tap_node['data'].get('label', 'N/A'))
        children = str(tap_node['data'].get('children', 'N/A'))
        weight = 100

        level = int(tap_node['data'].get('level', 'N/A'))
        level += 1
        level = str(level)

        custom1 = str(tap_node['data'].get('Productive?', 'N/A'))
        custom2 = str(tap_node['data'].get('Mood Impact', 'N/A'))
        custom3 = str(tap_node['data'].get('Fun Level', 'N/A'))

        # Add the new child node
        new_node = {
            'data': {
                'id': new_node_id,
                'label': new_label,
                'weight': weight,
                'level': level,
                'custom1': custom1,
                'custom2': custom2,
                'custom3': custom3
            }
        }
        # calculate weight


        # Add an edge to link the parent node (tapNode) to the new child node
        new_edge = {
            'data': {
                'source': tap_node['data']['id'],
                'target': new_node_id,
                'weight': 0
            }
        }

        # Append the new node and edge to the elements
        elements.append(new_node)
        elements.append(new_edge)

        return elements, name_store

    ### Delete function
    ### Delete function
    if remove_clicks > 0 and tap_node:
        # Get the ID of the tapped node to delete
        node_to_delete = tap_node['data']['id']

        # Check if no node is selected or if the selected node is the root node
        if node_to_delete == 'root' or tap_node is None:  # Replace 'root' with the actual ID of your root node
            return elements, name_store  # Do nothing and return the current state

        # Helper function to find all child nodes recursively
        def find_children(node_id, elements):
            children = []
            for element in elements:
                if 'source' in element['data'] and element['data']['source'] == node_id:
                    child_id = element['data']['target']
                    children.append(child_id)
                    children.extend(find_children(child_id, elements))  # Recursive call for nested children
            return children

        # Get all child node IDs
        nodes_to_delete = [node_to_delete] + find_children(node_to_delete, elements)

        # Filter elements to remove the nodes and their associated edges
        updated_elements = [
            element for element in elements
            if element['data']['id'] not in nodes_to_delete and
               ('source' not in element['data'] or element['data']['source'] not in nodes_to_delete)
        ]

        return updated_elements, name_store

    return elements, name_store
