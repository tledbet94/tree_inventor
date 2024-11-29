from dash import ctx, Input, Output, State
from app_instance import app


@app.callback(
    Output('weights-input-feedback', 'children'),
    [
        Input('weights-input-button', 'n_clicks'),
        Input('weights-input', 'value'),
        Input('cytoscape', 'selectedNodeData'),
        Input('cytoscape', 'selectedEdgeData')
    ],
    [
        State('manual-button', 'className'),
        State('auto-button', 'className'),

    ]
)
def update_main_screen(enter_clicks, user_input, selected_node, selected_edge, manual_class, auto_class):
    # Determine the mode
    user_feedback = 'Select an element to begin.'

    # Capture what the user needs to do
    user_feedback = ''
    element_selected = (selected_node or selected_edge) and \
                       (selected_node != '[]' or selected_edge != '[]')
    if not element_selected and not user_input:
        user_feedback = 'Please select an element and enter a weight.'
    elif not element_selected and user_input:
        user_feedback = 'Please select an element.'
    else:
        if user_input:
            user_feedback = 'You may enter your weight.'
        else:
            user_feedback = 'Please enter a weight.'

    screen_text = user_feedback

    if ctx.triggered_id == 'weights-input-button':
        screen_text = 'Weight entered.'

    return screen_text

