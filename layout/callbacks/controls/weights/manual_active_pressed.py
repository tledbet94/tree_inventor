from dash import callback, Input, Output, State
from app_instance import app

@app.callback(
    [Output('auto-button', 'className'),
     Output('manual-button', 'className')],
    [Input('auto-button', 'n_clicks'),
     Input('manual-button', 'n_clicks')],
    [State('auto-button', 'n_clicks_timestamp'),
     State('manual-button', 'n_clicks_timestamp')]
)
def update_manual_auto_buttons(auto_clicks, manual_clicks, auto_timestamp, manual_timestamp):
    # Handle None values for timestamps by setting them to -1
    auto_timestamp = auto_timestamp or -1
    manual_timestamp = manual_timestamp or -1

    # Determine which button has the most recent timestamp
    if auto_timestamp > manual_timestamp:
        return 'auto-manual-button active', 'auto-manual-button'
    elif manual_timestamp > auto_timestamp:
        return 'auto-manual-button', 'auto-manual-button active'
    else:
        # Default case when no button has been clicked
        return 'auto-manual-button active', 'auto-manual-button'
