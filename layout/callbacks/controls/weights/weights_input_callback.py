from dash import callback, Input, Output, State


@callback(
    [Output("weights-input", "className"),
     Output("weights-input-button", "className")],
    [Input("weights-input", "value"),
     Input("cytoscape", "tapNode")]

)
def show_weights_input(user_input, node_data):
    print(user_input)
    if node_data and user_input is None:
        print('test')
        return 'weights-input', 'hidden-opacity'
    elif node_data and (user_input is not None or ''):
        return 'weights-input', 'weights-input-button'
    else:
        return 'hidden-opacity', 'hidden-opacity'
