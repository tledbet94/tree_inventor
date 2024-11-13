from dash import Input, Output, State
from app_instance import app


# Description of callback
# The active state of a button will change if it is clicked
# Using timestamp to drive the active state to ensure only the most recent button is active

@app.callback(
    [Output('home-button', 'active'),
     Output('edit-button', 'active'),
     Output('algo-button', 'active'),
     Output('weights-button', 'active'),
     Output('active-button-store', 'data')],
    [Input('home-button', 'n_clicks'),
     Input('edit-button', 'n_clicks'),
     Input('algo-button', 'n_clicks'),
     Input('weights-button', 'n_clicks')],
    [State('home-button', 'n_clicks_timestamp'),
     State('edit-button', 'n_clicks_timestamp'),
     State('algo-button', 'n_clicks_timestamp'),
     State('weights-button', 'n_clicks_timestamp')]
)
def update_active_button(home_clicks, edit_clicks, algo_clicks, weights_clicks,
                         home_timestamp, edit_timestamp, algo_timestamp, weights_timestamp):
    # Handle None values for timestamps by setting them to -1
    home_timestamp = home_timestamp or -1
    edit_timestamp = edit_timestamp or -1
    algo_timestamp = algo_timestamp or -1
    weights_timestamp = weights_timestamp or -1

    # Determine which button has the most recent timestamp
    if (home_timestamp > edit_timestamp and
            home_timestamp > algo_timestamp and
            home_timestamp > weights_timestamp):
        return True, False, False, False, 'home'
    elif (edit_timestamp > home_timestamp and
          edit_timestamp > algo_timestamp and
          edit_timestamp > weights_timestamp):
        return False, True, False, False, 'edit'
    elif (algo_timestamp > home_timestamp and
          algo_timestamp > edit_timestamp and
          algo_timestamp > weights_timestamp):
        return False, False, True, False, 'algo'
    elif (weights_timestamp > home_timestamp and
          weights_timestamp > edit_timestamp and
          weights_timestamp > algo_timestamp):
        return False, False, False, True, 'weights'
    else:
        # Default case when no button has been clicked
        return False, False, False, False, 'none'
