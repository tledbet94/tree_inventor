from dash import Input, Output, State
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
        Input('template_one_button', 'n_clicks'),
        Input('template_two_button', 'n_clicks'),
        Input('template_three_button', 'n_clicks'),
        Input('template_four_button', 'n_clicks'),
        Input('template_five_button', 'n_clicks'),
        Input('template_six_button', 'n_clicks'),
        Input('template_seven_button', 'n_clicks'),
        Input('template_eight_button', 'n_clicks'),
    ],
    [
        State('template_one_button', 'n_clicks_timestamp'),
        State('template_two_button', 'n_clicks_timestamp'),
        State('template_three_button', 'n_clicks_timestamp'),
        State('template_four_button', 'n_clicks_timestamp'),
        State('template_five_button', 'n_clicks_timestamp'),
        State('template_six_button', 'n_clicks_timestamp'),
        State('template_seven_button', 'n_clicks_timestamp'),
        State('template_eight_button', 'n_clicks_timestamp')
    ]
)
def update_active_template_button(
        one_clicks, two_clicks, three_clicks, four_clicks,
        five_clicks, six_clicks, seven_clicks, eight_clicks,
        one_timestamp, two_timestamp, three_timestamp, four_timestamp,
        five_timestamp, six_timestamp, seven_timestamp, eight_timestamp
):
    # Handle None values for timestamps by setting them to -1
    timestamps = {
        'template_one': one_timestamp or -1,
        'template_two': two_timestamp or -1,
        'template_three': three_timestamp or -1,
        'template_four': four_timestamp or -1,
        'template_five': five_timestamp or -1,
        'template_six': six_timestamp or -1,
        'template_seven': seven_timestamp or -1,
        'template_eight': eight_timestamp or -1
    }

    # Determine the max timestamp
    max_timestamp = max(timestamps.values())

    # Check if all timestamps are -1 (no button clicked yet)
    if max_timestamp == -1:
        # Return False for all buttons
        return [False] * len(timestamps)

    # Generate active states for each button
    active_state = [timestamps[template] == max_timestamp for template in timestamps]
    print(active_state)

    # Return the active states
    return active_state
