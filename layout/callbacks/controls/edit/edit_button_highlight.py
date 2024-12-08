from dash import callback, Input, Output, State


@callback(
    [Output("rename-button", "className"),
     Output("add-button", "className"),
     Output("remove-button", "className"),
     Output("selected-edit", "data")],
    [Input("rename-button", "n_clicks"),
     Input("add-button", "n_clicks"),
     Input('remove-button', 'n_clicks')],
    [State("rename-button", "n_clicks_timestamp"),
     State('add-button', 'n_clicks_timestamp'),
     State("remove-button", "n_clicks_timestamp")]

)
def manage_edit_button_highlight(rename_clicks, add_clicks, remove_clicks,
                    rename_timestamp, add_timestamp, remove_timestamp):
    rename_timestamp = rename_timestamp or -1
    add_timestamp = add_timestamp or -1
    remove_timestamp = remove_timestamp or -1

    if rename_timestamp > add_timestamp and \
            rename_timestamp > remove_timestamp:
        return 'edit-button-selected', 'edit-button', 'edit-button', 'rename'

    elif add_timestamp > rename_timestamp and \
            add_timestamp > remove_timestamp:
        return 'edit-button', 'edit-button-selected', 'edit-button', 'add'

    elif remove_timestamp > rename_timestamp and \
            remove_timestamp > add_timestamp:
        return 'edit-button', 'edit-button', 'edit-button-selected', ''

    else:
        return 'edit-button', 'edit-button', 'edit-button', ''
