from dash import dcc, html, Input, Output, State, ctx
from app_instance import app

# Define the button in your layout
layout = html.Div([
    html.Button("Click Me", id="toggle-button", n_clicks=0, className="algo-button", style={"margin": "20px"}),
    dcc.Store(id='button-pressed-state', data=False)  # Store to manage button press state
])

# Callback to update the button appearance
@app.callback(
    Output("single-traversal-button", "className"),
    Input('traversal-output-display', 'children'),
)
def toggle_button_class(label):
    # Determine which Input triggered the callback
    if label != '':
        # Toggle pressed state
        pressed_state = not pressed_state
        # Update the store with the new state
        class_name = "algo-button active" if pressed_state else "algo-button"
        return class_name
    return "algo-button"

