from dash import callback_context, Input, Output, State
from app_instance import app


@app.callback(
    [
        Output('template_one_button', 'active'),
        Output('template_two_button', 'active'),
        Output('template_three_button', 'active'),
        Output('template_four_button', 'active'),
        Output('template_five_button', 'active'),
        Output('template_six_button', 'active'),
        Output('template_seven_button', 'active'),
        Output('template_eight_button', 'active'),
    ],
    [
        Input('starting-template-number', 'data'),
        Input('template_one_button', 'n_clicks'),
        Input('template_two_button', 'n_clicks'),
        Input('template_three_button', 'n_clicks'),
        Input('template_four_button', 'n_clicks'),
        Input('template_five_button', 'n_clicks'),
        Input('template_six_button', 'n_clicks'),
        Input('template_seven_button', 'n_clicks'),
        Input('template_eight_button', 'n_clicks'),
        Input('custom-fields-button', 'active'),
        Input('upload-area', 'contents')
        ],
    [
        State('template_one_button', 'active'),
        State('template_two_button', 'active'),
        State('template_three_button', 'active'),
        State('template_four_button', 'active'),
        State('template_five_button', 'active'),
        State('template_six_button', 'active'),
        State('template_seven_button', 'active'),
        State('template_eight_button', 'active'),
        State('upload-active', 'data')
    ]
)
def update_active_template_button(
        starting_number,
        one_clicks, two_clicks, three_clicks, four_clicks,
        five_clicks, six_clicks, seven_clicks, eight_clicks, upload, bottom_row_button_active,
        state_one, state_two, state_three, state_four, state_five, state_six, state_seven,
        state_eight, upload_active):
    # Initialize all buttons to inactive
    active_states = [False] * 8

    ctx = callback_context
    if ctx.triggered_id == 'upload-area' or upload_active:
        return active_states

    current_states = [state_one, state_two, state_three, state_four, state_five, state_six, state_seven, state_eight]

    # Check if any button has been clicked
    n_clicks = [
        one_clicks, two_clicks, three_clicks, four_clicks,
        five_clicks, six_clicks, seven_clicks, eight_clicks
    ]
    button_clicked = any(click > 0 for click in n_clicks if click is not None)

    if not ctx.triggered:
        # No trigger; return default inactive states
        return active_states

    # Get the ID of the Input that triggered the callback
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # List of button IDs in order
    button_ids = [
        'template_one_button',
        'template_two_button',
        'template_three_button',
        'template_four_button',
        'template_five_button',
        'template_six_button',
        'template_seven_button',
        'template_eight_button',
    ]

    if trigger_id == 'custom-fields-button' and not button_clicked:
        index = starting_number
        if index is not None:
            # Set the corresponding button to active
            active_states[index - 1] = True
    if trigger_id == 'custom-fields-button' and button_clicked:
        return current_states
    elif trigger_id in button_ids:
        active_states = [False] * 8
        # Triggered by one of the template buttons
        index = button_ids.index(trigger_id)
        active_states[index] = True
    else:
        # Some other trigger; return default inactive states
        pass

    return active_states
