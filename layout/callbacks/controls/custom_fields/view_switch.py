from dash import callback, Input, Output, State

@callback(
    [
        Output('field_names_view', 'style'),
        Output('field_values_view', 'style')
    ],
    [
        Input('field-names-button', 'className'),
        Input('field-values-button', 'className'),
    ]
)
def change_fields_view(names_class, values_class):

    visible = {'display': 'block'}
    hidden = {'display': 'none'}

    if names_class == 'fields-button active':
        return visible, hidden
    else:
        return hidden, visible
