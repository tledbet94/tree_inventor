from dash import callback, Input, Output


# ... [other imports and code]

@callback(
    [
        Output('single-traversal-button', 'disabled'),
        Output('multiple-traversal-button', 'disabled'),
        Output('home-button', 'disabled'),
        Output('edit-button', 'disabled'),
        Output('algo-button', 'disabled'),
        Output('algo-slider', 'disabled'),
        # Include other interactive components as needed
    ],
    [Input('traversal-running', 'data')]
)
def update_disabled_buttons(traversal_running):
    # If traversal_running is True, disable the buttons
    return [traversal_running] * 6  # Adjust the number to match the number of outputs