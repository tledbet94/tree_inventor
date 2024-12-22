from dash import callback, Input, Output


@callback(
    [
        Output('single-traversal-button', 'disabled'),
        Output('multiple-traversal-button', 'disabled'),
        Output('home-button', 'disabled'),
        Output('edit-button', 'disabled'),
        Output('algo-button', 'disabled'),
        Output('algo-slider', 'disabled'),
        Output('weights-button', 'disabled'),
        Output('templates-button', 'disabled'),
        Output('themes-button', 'disabled'),
        Output('user-button', 'disabled'),
        Output('save-load-button', 'disabled'),
        Output('change-view-button', 'disabled'),
        Output('custom-fields-button', 'disabled'),
        Output('ai-button', 'disabled'),
        Output('ai-update-button', 'disabled'),
        Output('ai-expand-button', 'disabled')
        # Include other interactive components as needed
    ],
    [Input('traversal-running', 'data')]
)
def update_disabled_buttons(traversal_running):
    # If traversal_running is True, disable the buttons
    return [traversal_running] * 16  # Adjust the number to match the number of outputs
