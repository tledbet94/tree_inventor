from dash import callback, Input, Output


@callback(
    [
        Output('field_names_view', 'style'),
        Output('field_values_view', 'style')
    ],
    [
        Input('field-names-button', 'active'),
        Input('field-values-button', 'active'),
    ]
)
def change_fields_view(names_active, values_active):
    # Define the styles for visibility
    visible = {'display': 'block'}
    hidden = {'display': 'none'}

    # Check which button is active and adjust visibility accordingly
    if names_active:
        return visible, hidden
    elif values_active:
        return hidden, visible
    else:
        # Default case: both views hidden (in case no button is active)
        return hidden, hidden
