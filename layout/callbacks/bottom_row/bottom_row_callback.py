from dash import Input, Output, State
from app_instance import app


# Description of callback
# The active state of a button will change if it is clicked
# This code is from ChatGPT o1-preview
# It suggested to use timestamp over n_clicks to drive the active state
# If it ain't broke, don't fix it . . .

@app.callback(
    [Output('home-button', 'active'),
     Output('edit-button', 'active'),
     Output('algo-button', 'active')],
    [Input('home-button', 'n_clicks'),
     Input('edit-button', 'n_clicks'),
     Input('algo-button', 'n_clicks')],
    [State('home-button', 'n_clicks_timestamp'),
     State('edit-button', 'n_clicks_timestamp'),
     State('algo-button', 'n_clicks_timestamp')]
)
def update_active_button(home_clicks, edit_clicks, algo_clicks,
                         home_timestamp, edit_timestamp, algo_timestamp):
    # Handle None values for timestamps
    home_timestamp = home_timestamp or -1
    edit_timestamp = edit_timestamp or -1
    algo_timestamp = algo_timestamp or -1

    # Find the most recent timestamp
    if (home_timestamp > edit_timestamp and
            home_timestamp > algo_timestamp):
        return True, False, False
    elif (edit_timestamp > home_timestamp and
          edit_timestamp > algo_timestamp):
        return False, True, False
    elif (algo_timestamp > home_timestamp and
          algo_timestamp > edit_timestamp):
        return False, False, True
    else:
        # Default case when no button has been clicked
        return False, False, False

