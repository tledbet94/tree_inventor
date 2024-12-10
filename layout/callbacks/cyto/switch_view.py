from dash import callback, Input, Output, State

cytoscape_background_color = '#352b42'

# Predefined styles
default_cyto_style = {
    'height': '72vh',
    'width': '100%',
    'backgroundColor': cytoscape_background_color,
    'border': '15px solid #868188',
    'borderRadius': '30px',
    'box-shadow': 'inset 0px 0px 10px 10px #646365'
}
full_screen_cyto_style = {
    'height': '100vh',
    'width': '100%',
    'backgroundColor': cytoscape_background_color,
    'border': '15px solid #868188',
    'borderRadius': '30px',
    'box-shadow': 'inset 0px 0px 10px 10px #646365'
}
default_control_style = {'padding': '0', 'height': '100%', 'display': 'flex'}
hidden_control_style = {'padding': '0', 'height': '100%', 'display': 'none'}

@callback(
    [
        Output('cytoscape', 'style'),
        Output('cyto-col', 'width'),
        Output('control-col', 'style')
    ],
    [
        Input('change-view-button', 'n_clicks'),
        Input('orientation-store', 'data')
    ],
    State('cyto-col', 'width'),
    prevent_initial_call=True
)
def change_cyto_view(n_clicks, orientation, current_cyto_width):
    if orientation == 'portrait' or (orientation == 'landscape' and (n_clicks or 0) > 0):
        return full_screen_cyto_style, 12, hidden_control_style
    elif current_cyto_width == 12 and (n_clicks or 0) > 0:
        return default_cyto_style, 9, default_control_style
    else:
        return default_cyto_style, 9, default_control_style
