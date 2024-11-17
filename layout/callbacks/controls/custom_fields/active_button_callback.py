from dash import callback, Input, Output, State

@callback(
    [Output('field-names-button', 'className'),
     Output('field-values-button', 'className')],
    [Input('field-names-button', 'n_clicks'),
     Input('field-values-button', 'n_clicks')],
    [State('field-names-button', 'n_clicks_timestamp'),
     State('field-values-button', 'n_clicks_timestamp')]
)
def update_fields_buttons(fields_names_clicks, fields_values_clicks, fields_names_timestamp, fields_values_timestamp):
    print('test')
    # Handle None values for timestamps by setting them to -1
    fields_names_timestamp = fields_names_timestamp or -1
    fields_values_timestamp = fields_values_timestamp or -1

    # Determine which button has the most recent timestamp
    if fields_names_timestamp > fields_values_timestamp:
        return 'fields-button active', 'fields-button'
    elif fields_values_timestamp > fields_names_timestamp:
        return 'fields-button', 'fields-button active'
    else:
        # Default case when no button has been clicked
        return 'fields-button active', 'fields-button'
