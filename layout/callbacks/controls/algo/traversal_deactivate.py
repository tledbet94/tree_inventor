from dash import callback, Input, Output
from app_instance import app

@app.callback(
    [
        Output('single-traversal-button', 'disabled'),
        Output('multiple-traversal-button', 'disabled'),
        Output('home-button', 'disabled'),
        Output('edit-button', 'disabled'),
        Output('algo-button', 'disabled'),
        Output('algo-slider', 'disabled'),
        Output('weights-button', 'disabled'),
        Output('auto-button', 'disabled'),
        # Include other interactive components as needed
    ],
    [Input('traversal-running', 'data')]
)
def update_disabled_buttons(traversal_running):
    # If traversal_running is True, disable the buttons
    return [traversal_running] * 8  # Adjust the number to match the number of outputs
