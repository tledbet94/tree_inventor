from dash import callback, ctx, Input, Output, State


# Callback to update cytoscape elements with the latest modified store's data
@callback(
    Output('cytoscape', 'elements'),
    [
        Input('buttons-store', 'data'),
        Input('edit-store', 'data'),
        Input('single-interval-store', 'data'),
        Input('multiple-interval-store', 'data'),
        Input('fields-store', 'data'),
        Input('template-store', 'data'),
        Input('upload-store', 'data'),
        Input('weights-store', 'data'),
        Input('cytoscape', 'tapNode'),
        Input('cytoscape', 'tapEdge')
    ],
    State('cytoscape', 'elements')
)
def update_cytoscape_elements(buttons_elements, edit_elements, single_interval_elements,
                              multiple_interval_elements, fields_elements,
                              template_elements, uploaded_elements, weights_elements,
                              tap_node, tap_edge, current_elements):
    # Determine which Input triggered the callback
    triggered_prop_id = ctx.triggered[0]['prop_id'] if ctx.triggered else None

    if triggered_prop_id == 'cytoscape.tapNode':
        clicked_id = tap_node['data']['id']

        # Update the elements
        for element in current_elements:
            if element['data']['id'] == clicked_id:
                element['data']['last_clicked'] = 'True'
            else:
                element['data']['last_clicked'] = 'False'
        return current_elements

    elif triggered_prop_id == 'cytoscape.tapEdge':
        clicked_id = tap_edge['data']['id']

        # Update the elements
        for element in current_elements:
            if element['data']['id'] == clicked_id:
                element['data']['last_clicked'] = 'True'
            else:
                element['data']['last_clicked'] = 'False'
        return current_elements

    elif triggered_prop_id == 'buttons-store.data':
        return buttons_elements
    elif triggered_prop_id == 'edit-store.data':
        return edit_elements

    elif triggered_prop_id == 'single-interval-store.data':
        return single_interval_elements

    elif triggered_prop_id == 'multiple-interval-store.data':
        return multiple_interval_elements

    elif triggered_prop_id == 'fields-store.data':
        return fields_elements

    elif triggered_prop_id == 'template-store.data':
        return template_elements

    elif triggered_prop_id == 'upload-store.data':
        return uploaded_elements

    elif triggered_prop_id == 'weights-store.data':
        return weights_elements

    else:
        # If no inputs triggered, return the current elements
        return current_elements
