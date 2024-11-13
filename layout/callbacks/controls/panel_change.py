# panel_change.py
from dash import callback_context, Input, Output
from app_instance import app

@app.callback(
    Output('home-mode', 'style'),
    Output('edit-mode', 'style'),
    Output('algo-mode', 'style'),
    Output('weights-mode', 'style'),
    [Input('home-button', 'n_clicks'),
     Input('edit-button', 'n_clicks'),
     Input('algo-button', 'n_clicks'),
     Input('weights-button', 'n_clicks')],
)
def update_mode(home_clicks, edit_clicks, algo_clicks, weights_clicks):
    ctx = callback_context

    if not ctx.triggered:
        button_id = 'home-button'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'home-button':
        return {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    elif button_id == 'edit-button':
        return {'display': 'none'}, {'display': 'block'}, {'display': 'none'}, {'display': 'none'}
    elif button_id == 'algo-button':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, {'display': 'none'}
    elif button_id == 'weights-button':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'block'}
    else:
        return {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
