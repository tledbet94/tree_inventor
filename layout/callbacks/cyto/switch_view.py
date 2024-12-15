from dash import callback, Input, Output, State

cytoscape_background_color = '#352b42'


default_control_style = {'padding': '0', 'height': '100%', 'display': 'flex'}
hidden_control_style = {'padding': '0', 'height': '100%', 'display': 'none'}

# Callback to switch between classes for Cytoscape
@callback(
    [
        Output('cytoscape', 'className'),
        Output('cyto-col', 'width'),
        Output('control-col', 'className'),
        Output('change-view-button', 'n_clicks'),
        Output('view-warning-text', 'children')
    ],
    [
        Input('change-view-button', 'n_clicks'),
        Input('orientation-store', 'data')
    ],
    [
        State('cyto-col', 'width'),
    ]
)
def change_cyto_view(n_clicks, orientation, current_cyto_width):
    if orientation == 'portrait' or (current_cyto_width == 9 and (n_clicks or 0) > 0):
        if orientation == 'portrait':
            return 'full-screen-cyto-style', 12, 'hidden-control-style', 0, 'ROTATE TO SWITCH'
        else:
            return 'full-screen-cyto-style', 12, 'hidden-control-style', 0, ''
    elif current_cyto_width == 12 and (n_clicks or 0) > 0:
        return 'default-cyto-style', 9, 'default-control-style', 0, ''
    elif current_cyto_width == 12 and (n_clicks or 0) == 0:
        return 'full-screen-cyto-style', 12, 'hidden-control-style', 0, ''
    else:
        return 'default-cyto-style', 9, 'default-control-style', 0, ''
