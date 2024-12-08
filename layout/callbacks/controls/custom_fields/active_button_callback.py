from dash import callback, Input, Output, State


@callback(
    [Output('field-names-button', 'active'),
     Output('field-values-button', 'active')],
    [Input('field-names-button', 'n_clicks'),
     Input('field-values-button', 'n_clicks')],
    [State('field-names-button', 'n_clicks_timestamp'),
     State('field-values-button', 'n_clicks_timestamp')]
)
def update_fields_buttons(names_clicks, values_clicks, names_timestamp, values_timestamp):

    names_timestamp = names_timestamp or -1
    values_timestamp = values_timestamp or -1

    if names_timestamp > values_timestamp:
        return True, False

    elif values_timestamp > names_timestamp:
        return False, True

    else:
        return True, False
