# panel_change.py
from dash import callback, callback_context, Input, Output

@callback(
    Output('home-mode', 'style'),
    Output('save-load-mode', 'style'),
    Output('edit-mode', 'style'),
    Output('algo-mode', 'style'),
    Output('weights-mode', 'style'),
    Output('custom-fields-mode', 'style'),
    Output('templates-mode', 'style'),
    Output('themes-mode', 'style'),
    Output('user-mode', 'style'),
    Output('settings-mode', 'style'),
    Output('ai-mode', 'style'),    # <-- New output for AI mode
    [
        Input('home-button', 'n_clicks'),
        Input('edit-button', 'n_clicks'),
        Input('algo-button', 'n_clicks'),
        Input('weights-button', 'n_clicks'),
        Input('save-load-button', 'n_clicks'),
        Input('custom-fields-button', 'n_clicks'),
        Input('templates-button', 'n_clicks'),
        Input('themes-button', 'n_clicks'),
        Input('user-button', 'n_clicks'),
        Input('settings-button', 'n_clicks'),
        Input('ai-button', 'n_clicks'),  # <-- New input for AI button
    ],
)
def update_mode(
    home_clicks, edit_clicks, algo_clicks, weights_clicks,
    save_load_clicks, custom_fields_clicks, templates_clicks,
    themes_clicks, user_clicks, settings_clicks, ai_clicks
):
    ctx = callback_context

    # Determine which button was clicked
    if not ctx.triggered:
        button_id = 'home-button'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Update styles based on clicked button
    if button_id == 'home-button':
        return (
            {'display': 'block'},  # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'edit-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'block'},  # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'algo-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'block'},  # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'weights-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'block'},  # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'save-load-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'block'},  # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'custom-fields-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'block'},  # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'templates-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'block'},  # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'themes-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'block'},  # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'user-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'block'},  # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'settings-button':
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'block'},  # settings-mode
            {'display': 'none'},   # ai-mode
        )
    elif button_id == 'ai-button':  # <-- New AI button check
        return (
            {'display': 'none'},   # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'block'},  # ai-mode
        )
    else:
        # Default case if no recognized button is clicked
        return (
            {'display': 'block'},  # home-mode
            {'display': 'none'},   # save-load-mode
            {'display': 'none'},   # edit-mode
            {'display': 'none'},   # algo-mode
            {'display': 'none'},   # weights-mode
            {'display': 'none'},   # custom-fields-mode
            {'display': 'none'},   # templates-mode
            {'display': 'none'},   # themes-mode
            {'display': 'none'},   # user-mode
            {'display': 'none'},   # settings-mode
            {'display': 'none'},   # ai-mode
        )
