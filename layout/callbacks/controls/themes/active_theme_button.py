from dash import callback, Input, Output, State, callback_context

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


# Add an Input for the file-info store
@callback(
    outputs,
    inputs + [Input('file-info', 'data')]
)
def update_buttons(*args):
    # The last argument is the theme-info data
    file_info_data = args[-1]
    theme_info_data = file_info_data['theme_data']
    # The rest are the n_clicks_timestamps for the buttons
    n_clicks_timestamps = args[:-1]

    # Map button IDs to their n_clicks_timestamp
    n_clicks_ts_dict = dict(zip(button_ids, n_clicks_timestamps))

    # Extract the current theme settings from file_info_data if available
    # Provide a safe fallback if theme_data is not present
    theme_data = theme_info_data if theme_info_data else {}

    # Expected theme_data keys and their corresponding groups
    # We assume that theme_data keys match group keys, except 'shapes' vs 'shape' in theme_data.
    # Adjust accordingly if the keys differ.
    theme_map = {
        'colors': theme_data.get('color', ''),
        'shapes': theme_data.get('shape', ''),
        'outlines': theme_data.get('outline', ''),
        'pointers': theme_data.get('pointer', ''),
        'background': theme_data.get('background', '')
    }
    active_states = []

    for group_name, group_buttons in groups.items():
        # Get n_clicks_timestamp for buttons in this group
        group_n_clicks_ts = [n_clicks_ts_dict[btn_id] or 0 for btn_id in group_buttons]

        if any(group_n_clicks_ts):
            # A button in this group has been clicked
            # Find the button with the most recent timestamp
            max_timestamp = max(group_n_clicks_ts)
            group_active_states = [ts == max_timestamp for ts in group_n_clicks_ts]
        else:
            # No button in this group has been clicked yet; use the theme_data to find the active button
            desired_value = theme_map.get(group_name, '')
            # Attempt to find a button that corresponds to the theme_data value
            # This depends on how you map theme_data values to button IDs.
            # For example, if theme_data['colors'] = 'blue' and the button is 'blueberry-button',
            # you might need to implement a matching logic. Here we do a simple "contains" check.

            matched_index = None
            # Simple heuristic: check if the theme_data value is contained in the button ID
            # Adjust this logic to fit your naming conventions.
            for i, btn_id in enumerate(group_buttons):
                # Normalize naming if needed. For instance:
                # - For colors: theme_data might say 'blue' and button is 'blueberry-button'
                # - For shapes: theme_data might say 'square' and button is 'square-button'
                if desired_value and desired_value.replace('-', '_') in btn_id:
                    matched_index = i
                    break

            if matched_index is not None:
                # We found a suitable match
                group_active_states = [i == matched_index for i in range(len(group_buttons))]
            else:
                # If we cannot match, fall back to the default (first button)
                group_active_states = [True] + [False] * (len(group_buttons) - 1)

        active_states.extend(group_active_states)
    return active_states
