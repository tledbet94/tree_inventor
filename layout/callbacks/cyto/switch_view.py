from dash import callback, Input, Output, State

cytoscape_background_color = '#352b42'

# Predefined styles
default_cyto_style = {
    'height': '52vh',
    'width': '100%',
    'backgroundColor': cytoscape_background_color,
    'border': '3px solid #868188',
    'borderRadius': '30px',
    'box-shadow': 'inset 0px 0px 10px 10px #646365',
    'flex': '1'
}
full_screen_cyto_style = {
    'height': '95vh',
    'width': '100%',
    'backgroundColor': cytoscape_background_color,
    'border': '3px solid #868188',
    'borderRadius': '30px',
    'box-shadow': 'inset 0px 0px 10px 10px #646365',
    'flex': '1'
}
default_control_style = {'padding': '0', 'height': '100%', 'display': 'flex'}
hidden_control_style = {'padding': '0', 'height': '100%', 'display': 'none'}


# use active instead of n clicks to control state
@callback(
    [
        Output('cytoscape', 'style'),
        Output('cyto-col', 'width'),
        Output('control-col', 'style'),
        Output('change-view-button', 'n_clicks')
    ],
    [
        Input('change-view-button', 'n_clicks'),
        Input('orientation-store', 'data')
    ],
    [
        State('cytoscape', 'style'),
        State('cyto-col', 'width'),
        State('control-col', 'style'),
    ]
)
def change_cyto_view(n_clicks, orientation, current_cyto_style, current_cyto_width, current_control_style):
    if orientation == 'portrait' or (current_cyto_width == 9 and (n_clicks or 0) > 0):
        return full_screen_cyto_style, 12, hidden_control_style, 0
    elif current_cyto_width == 12 and (n_clicks or 0) > 0:
        print('switch back')
        return default_cyto_style, 9, default_control_style, 0
    elif current_cyto_width == 12 and (n_clicks or 0) == 0:
        print('in alt view')
        return full_screen_cyto_style, 12, hidden_control_style, 0
    else:
        print('base case')
        return default_cyto_style, 9, default_control_style, 0
