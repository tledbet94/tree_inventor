from dash import callback, Input, Output, State


@callback(
    [Output('field-names-button', 'active'),
     Output('field-values-button', 'active')],
    [Input('field-names-button', 'n_clicks'),
     Input('field-values-button', 'n_clicks')],
    [State('field-names-button', 'n_clicks_timestamp'),
     State('field-values-button', 'n_clicks_timestamp')]
)
def update_fields_buttons(names_clicks, values_clicks):
    names_clicks = names_clicks or 0
    values_clicks = values_clicks or 0

    if names_clicks == 0 and values_clicks == 0:
        # Default state when the app loads
        return True, False
    elif names_clicks > values_clicks:
        return True, False
    else:
        return False, True
