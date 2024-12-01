from dash import Input, Output, State
from app_instance import app
import copy

# Description of callback
# The active state of a button will change if it is clicked
# Using timestamp to drive the active state to ensure only the most recent button is active

@app.callback(
    [
        Output('buttons-store', 'data'),
        Output('home-button', 'active'),
        Output('edit-button', 'active'),
        Output('algo-button', 'active'),
        Output('weights-button', 'active'),
        Output('custom-fields-button', 'active'),
        Output('templates-button', 'active'),
        Output('themes-button', 'active'),
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
        Input('themes-button', 'n_clicks'),
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
        State('themes-button', 'n_clicks_timestamp'),
        State('settings-button', 'n_clicks_timestamp'),
        State('save-load-button', 'n_clicks_timestamp'),
        State('user-button', 'n_clicks_timestamp'),
        State('cytoscape', 'elements')
    ]
)
def update_active_button(
        home_clicks, edit_clicks, algo_clicks, weights_clicks,
        custom_fields_clicks, templates_clicks, theme_clicks, settings_clicks, save_load_clicks, user_clicks,
        home_timestamp, edit_timestamp, algo_timestamp, weights_timestamp,
        custom_fields_timestamp, templates_timestamp, theme_timestamp, settings_timestamp, save_load_timestamp,
        user_timestamp, elements
):
    # Reset tree styles
    elements = copy.deepcopy(elements) if elements is not None else []
    for element in elements:
        element['data']['traversed'] = 'False'
        element['data']['common'] = 'False'

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

    buttons = ['home', 'edit', 'algo', 'weights', 'custom_fields', 'templates', 'theme', 'settings', 'save_load', 'user']

    if max_timestamp == -1:
        # At app start, set 'home' as active
        active_button_name = 'home'
        active_states = [button == 'home' for button in buttons]
    else:
        # Find the buttons that have the max timestamp (handles simultaneous clicks)
        clicked_buttons = [button for button, timestamp in timestamps.items() if timestamp == max_timestamp]
        active_button_name = clicked_buttons[0]  # Choose the first one in case of tie

        # Generate active states for each button
        active_states = [timestamps[button] == max_timestamp for button in buttons]

    # Return the active states and the name of the active button
    return (
        elements,       # buttons-store
        *active_states, # Active states for each button
        active_button_name  # active-button-store
    )
