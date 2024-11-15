from dash import callback, Input, Output

neither_node_nor_input = 'Select a Node and enter a weight.'
only_node = 'Enter a weight.'
both_selected = 'Press enter to apply weight.'


@callback(
    [Output("weights-input-feedback", "children"),
     Output("weights-input", "className"),
     Output("weights-input-button", "className"),
     Output('manual-auto-row', 'className'),
     Output('manual-feedback-row', 'className'),
     Output('weights-progress-row', 'className')],
    [Input("weights-input", "value"),
     Input("cytoscape", "tapNode"),
     Input("cytoscape", "tapEdge"),
     Input('manual-button', 'className')]

)
def show_weights_input(user_input, node_data, edge_data, manual_class):
    manual_active = False
    if manual_class == 'auto-manual-button active':
        manual_active = True

    if (node_data or edge_data) and user_input is None and manual_active is False:
        return (neither_node_nor_input, 'weights-input', 'hidden-opacity',
                'visible-opacity',
                'hidden-opacity', 'hidden-opacity',)
    elif (node_data or edge_data) and user_input is None and manual_active is True:
        return (neither_node_nor_input, 'weights-input', 'hidden-opacity',
                'visible-opacity',
                'visible-opacity', 'visible-opacity',)
    elif (node_data or edge_data) and (user_input is not None or '') and manual_active is False:
        return (only_node, 'weights-input', 'weights-input-button',
                'visible-opacity',
                'hidden-opacity', 'hidden-opacity')
    elif (node_data or edge_data) and (user_input is not None or '') and manual_active is True:
        return (only_node, 'weights-input', 'weights-input-button',
                'visible-opacity',
                'visible-opacity', 'visible-opacity')
    else:
        return (neither_node_nor_input, 'hidden-opacity', 'hidden-opacity',
                'hidden-opacity',
                'hidden-opacity', 'hidden-opacity')
