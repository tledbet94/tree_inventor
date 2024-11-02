from dash import Input, Output, State
from app_instance import app

from layout.elements.control_panel.modes.home import home
from layout.elements.control_panel.modes.edit import edit


# Description of callback
# -This should trigger when a button is pressed
# -The active property of a button changing represents being pressed
# -The active property is being updated in button_row_callback
# -A change in active button results in a change in the "mode" of the control panel

@app.callback(
    Output('control-panel', 'children'),
    [Input('home-button', 'active'),
     Input('edit-button', 'active')],
    State('control-panel', 'children')
)
def update_mode(home_active, edit_active, current_mode):
    # at start
    if home_active:
        print('home active')
        return home
    elif edit_active:
        print('edit active')
        return edit
    else:
        return current_mode
