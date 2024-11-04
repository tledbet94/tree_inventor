from dash import html
import dash_bootstrap_components as dbc

node_label = html.P('Label:', className='info-text-label')
node_name = html.P(id='node-name', className='info-text-actual')

weight_label = html.P('Weight:', className='info-text-label')
weight_actual = html.P(id='node-weight', className='info-text-actual')

level_label = html.P('Level:', className='info-text-label')
level_actual = html.P(id='node-level', className='info-text-actual')

custom1_label = html.P('Custom 1:', className='info-text-label')
custom1_actual = html.P(id='node-custom1', className='info-text-actual')

custom2_label = html.P('Custom 2:', className='info-text-label')
custom2_actual = html.P(id='node-custom2', className='info-text-actual')

custom3_label = html.P('Custom 3:', className='info-text-label')
custom3_actual = html.P(id='node-custom3', className='info-text-actual')

first_row = dbc.Row([dbc.Col(node_label), dbc.Col(node_name),
                     dbc.Col(custom1_label), dbc.Col(custom1_actual)])

second_row = dbc.Row([dbc.Col(weight_label), dbc.Col(weight_actual),
                      dbc.Col(custom2_label), dbc.Col(custom2_actual)])

third_row = dbc.Row([dbc.Col(level_label), dbc.Col(level_actual),
                     dbc.Col(custom3_label), dbc.Col(custom3_actual)])

info_contents = html.Div([first_row, second_row, third_row])
