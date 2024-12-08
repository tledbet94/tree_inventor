from dash import callback, Input, Output


@callback(
    [Output("weights-input", "className"),
     Output("weights-input-button", "className"),
     Output('manual-auto-row', 'className'),
     Output('manual-feedback-row', 'className'),
     Output('weights-progress-row', 'className')],
    [Input("weights-input", "value"),
     Input("cytoscape", "selectedNodeData"),
     Input("cytoscape", "selectedEdgeData"),
     Input('manual-button', 'className')]

)
def show_weights_input(user_input, selected_node, selected_edge, manual_class):
    manual_active = False
    if manual_class == 'auto-manual-button active':
        manual_active = True

    element_selected = (selected_node or selected_edge) and \
                       (selected_node != '[]' or selected_edge != '[]')

    if not element_selected:
        return ('hidden-opacity', 'hidden-opacity',
                'hidden-opacity',
                'hidden-opacity', 'hidden-opacity')
    elif element_selected and user_input is None and manual_active is False:
        return ('weights-input', 'hidden-opacity',
                'visible-opacity',
                'hidden-opacity', 'hidden-opacity',)
    elif element_selected and (user_input is not None or '') and manual_active is False:
        return ('weights-input', 'weights-input-button',
                'visible-opacity',
                'hidden-opacity', 'hidden-opacity')
    elif element_selected and user_input is None and manual_active is True:
        return ('weights-input', 'hidden-opacity',
                'visible-opacity',
                'visible-opacity', 'visible-opacity',)
    elif element_selected and (user_input is not None or '') and manual_active is True:
        return ('weights-input', 'weights-input-button',
                'visible-opacity',
                'visible-opacity', 'visible-opacity')
    else:
        return ('hidden-opacity', 'hidden-opacity',
                'hidden-opacity',
                'hidden-opacity', 'hidden-opacity')
