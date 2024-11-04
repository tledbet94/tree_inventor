from dash import Input, Output, State
from app_instance import app


@app.callback(
    [Output("edit-input-row", "className"),
     Output("edit-input-feedback-row", "className")],
    [Input("rename-button", "n_clicks"),
     Input("add-button", "n_clicks"),
     Input('remove-button', 'n_clicks')],
    [State("rename-button", "n_clicks_timestamp"),
     State("add-button", "n_clicks_timestamp"),
     State('remove-button', 'n_clicks_timestamp')]
)
def show_edit_input(rename_clicks, add_clicks, remove_clicks,
                    rename_timestamp, add_timestamp, remove_timestamp):
    rename_timestamp = rename_timestamp or -1
    add_timestamp = add_timestamp or -1
    remove_timestamp = remove_timestamp or -1

    if rename_timestamp > remove_timestamp or \
            add_timestamp > remove_timestamp:
        return 'visible-opacity', 'visible-opacity'
    elif remove_timestamp > rename_timestamp and \
            remove_timestamp > add_timestamp:
        return 'hidden-opacity', 'hidden-opacity'
    else:
        return 'hidden-opacity', 'hidden-opacity'


@app.callback(
    [Output("edit-input-feedback", "children"),
     Output("edit-input-button", "className"),
     Output("edit-enter-click-store", "data"),
     Output("edit-input", "value"), ],
    [Input("cytoscape", "tapNode"),
     Input("edit-input", "value"),
     Input('edit-input-button', 'n_clicks')],
    State('edit-enter-click-store', 'data')
)
def edit_check_input(selected_node, user_input, enter_clicks, stored_enter_clicks):
    enter_clicks = enter_clicks or 0

    if enter_clicks > stored_enter_clicks:
        return 'TREE MODIFIED | Waiting for user input', 'hidden-opacity', (stored_enter_clicks + 1), ''
    if selected_node:
        if user_input and user_input.strip() != '':
            return 'VALID |\n Node selected and input detected', 'edit-input-button', stored_enter_clicks, user_input
        else:
            return 'INVALID |\n No user input', 'hidden-opacity', stored_enter_clicks, user_input
    else:
        return 'INVALID |\n No node selected', 'hidden-opacity', stored_enter_clicks, user_input
