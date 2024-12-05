from dash import Input, Output, callback_context
from app_instance import app

# Define the groups
groups = {
    'colors': ['blueberry-button', 'banana-button', 'grape-button', 'orange-button'],
    'shapes': ['circle-button', 'triangle-button', 'square-button', 'octagon-button'],
    'outlines': ['single-outline-button', 'no-outline-button', 'shadow-button', 'double-button'],
    'pointers': ['circle-pointer-button', 'no-pointer-button', 'arrow-pointer-button', 'tee-pointer-button'],
    'background': ['blue_background_button', 'brown_background_button',
                   'green_background_button', 'black_background_button']
}

# Flatten the list of button IDs
button_ids = [button_id for group in groups.values() for button_id in group]

# Create Outputs dynamically based on button IDs
outputs = [Output(button_id, 'active') for button_id in button_ids]

# Create Inputs dynamically based on button IDs using 'n_clicks_timestamp'
inputs = [Input(button_id, 'n_clicks_timestamp') for button_id in button_ids]


@app.callback(outputs, inputs)
def update_buttons(*n_clicks_timestamps):
    # Map button IDs to their n_clicks_timestamp
    n_clicks_ts_dict = dict(zip(button_ids, n_clicks_timestamps))

    # Initialize the list to store the 'active' state of each button
    active_states = []

    for group_buttons in groups.values():
        # Get n_clicks_timestamp for buttons in this group
        group_n_clicks_ts = [n_clicks_ts_dict[btn_id] or 0 for btn_id in group_buttons]

        if any(group_n_clicks_ts):
            # A button in this group has been clicked
            # Find the button with the most recent timestamp
            max_timestamp = max(group_n_clicks_ts)
            group_active_states = [ts == max_timestamp for ts in group_n_clicks_ts]
        else:
            # No button in this group has been clicked yet; activate the first button
            group_active_states = [True] + [False] * (len(group_buttons) - 1)

        active_states.extend(group_active_states)

    return active_states
