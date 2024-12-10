from dash import dcc, html
import dash_bootstrap_components as dbc

node_label = html.P('Label:', id='info-label', className='info-text-label')
node_name = html.P(id='node-name', className='info-text-actual')

weight_label = html.P('Weight:', className='info-text-label')
weight_actual = html.P(id='node-weight', className='info-text-actual')

level_label = html.P('Level:', className='info-text-label')
level_actual = html.P(id='node-level', className='info-text-actual')

custom1_label = html.P(id='info-custom1-label', children='Custom 1:', className='info-text-label')
custom1_actual = html.P(id='node-custom1', className='info-text-actual')

custom2_label = html.P(id='info-custom2-label', children='Custom 2:', className='info-text-label')
custom2_actual = html.P(id='node-custom2', className='info-text-actual')

custom3_label = html.P(id='info-custom3-label', children='Custom 3:', className='info-text-label')
custom3_actual = html.P(id='node-custom3', className='info-text-actual')

change_screen = dbc.Button(children='SWITCH', id='change-view-button', className='switch-button')

first_row = dbc.Row([dbc.Col(node_label), dbc.Col(node_name),
                     dbc.Col(custom1_label), dbc.Col(custom1_actual), dbc.Col(change_screen, width=1)])

second_row = dbc.Row([dbc.Col(weight_label), dbc.Col(weight_actual),
                      dbc.Col(custom2_label), dbc.Col(custom2_actual), dbc.Col(width=1)], id='info_row_two')

third_row = dbc.Row([dbc.Col(level_label), dbc.Col(level_actual),
                     dbc.Col(custom3_label), dbc.Col(custom3_actual), dbc.Col(width=1)], id='info_row_three')

info_contents = dbc.Container([dcc.Store(id='info-panel-data'),
                               first_row, second_row, third_row], fluid=True, className='info-div')
