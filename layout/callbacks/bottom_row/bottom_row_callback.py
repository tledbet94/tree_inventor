from dash import Input, Output, State
from app_instance import app

# Description of callback
# The active state of a button will change if it is clicked
# Using timestamp to drive the active state to ensure only the most recent button is active

@app.callback(
    [
        Output('home-button', 'active'),
        Output('edit-button', 'active'),
        Output('algo-button', 'active'),
        Output('weights-button', 'active'),
        Output('custom-fields-button', 'active'),
        Output('templates-button', 'active'),
        Output('theme-button', 'active'),
        Output('settings-button', 'active'),
        Output('save-load-button', 'active'),
        Output('user-button', 'active'),
        Output('active-button-store', 'data')
    ],
    [
        Input('home-button', 'n_clicks'),
        Input('edit-button', 'n_clicks'),
        Input('algo-button', 'n_clicks'),
        Input('weights-button', 'n_clicks'),
        Input('custom-fields-button', 'n_clicks'),
        Input('templates-button', 'n_clicks'),
        Input('theme-button', 'n_clicks'),
        Input('settings-button', 'n_clicks'),
        Input('save-load-button', 'n_clicks'),
        Input('user-button', 'n_clicks')
    ],
    [
        State('home-button', 'n_clicks_timestamp'),
        State('edit-button', 'n_clicks_timestamp'),
        State('algo-button', 'n_clicks_timestamp'),
        State('weights-button', 'n_clicks_timestamp'),
        State('custom-fields-button', 'n_clicks_timestamp'),
        State('templates-button', 'n_clicks_timestamp'),
        State('theme-button', 'n_clicks_timestamp'),
        State('settings-button', 'n_clicks_timestamp'),
        State('save-load-button', 'n_clicks_timestamp'),
        State('user-button', 'n_clicks_timestamp')
    ]
)
def update_active_button(
    home_clicks, edit_clicks, algo_clicks, weights_clicks,
    custom_fields_clicks, templates_clicks, theme_clicks, settings_clicks, save_load_clicks, user_clicks,
    home_timestamp, edit_timestamp, algo_timestamp, weights_timestamp,
    custom_fields_timestamp, templates_timestamp, theme_timestamp, settings_timestamp, save_load_timestamp, user_timestamp
):
    # Handle None values for timestamps by setting them to -1
    home_timestamp = home_timestamp or -1
    edit_timestamp = edit_timestamp or -1
    algo_timestamp = algo_timestamp or -1
    weights_timestamp = weights_timestamp or -1
    custom_fields_timestamp = custom_fields_timestamp or -1
    templates_timestamp = templates_timestamp or -1
    theme_timestamp = theme_timestamp or -1
    settings_timestamp = settings_timestamp or -1
    save_load_timestamp = save_load_timestamp or -1
    user_timestamp = user_timestamp or -1

    # Create a dictionary of timestamps
    timestamps = {
        'home': home_timestamp,
        'edit': edit_timestamp,
        'algo': algo_timestamp,
        'weights': weights_timestamp,
        'custom_fields': custom_fields_timestamp,
        'templates': templates_timestamp,
        'theme': theme_timestamp,
        'settings': settings_timestamp,
        'save_load': save_load_timestamp,
        'user': user_timestamp
    }

    # Determine the button with the most recent timestamp
    max_timestamp = max(timestamps.values())

    if max_timestamp == -1:
        active_button_name = 'none'
    else:
        # Find all buttons that have the max timestamp (handles simultaneous clicks)
        clicked_buttons = [button for button, timestamp in timestamps.items() if timestamp == max_timestamp]
        active_button_name = clicked_buttons[0]  # Choose the first one in case of tie

    # Generate active states for each button
    buttons = ['home', 'edit', 'algo', 'weights', 'custom_fields', 'templates', 'theme', 'settings', 'save_load', 'user']
    active_states = [timestamps[button] == max_timestamp and max_timestamp != -1 for button in buttons]

    # Return the active states and the name of the active button
    return active_states + [active_button_name]
