from dash import html
import dash_bootstrap_components as dbc

# 1st column
node_label = html.P('Element:', className='info-text')
node_name = html.P(id='node-name', className='info-text')

# 2nd column
weight_label = html.P('Weight:', className='info-text')
weight_actual = html.P(id='node-weight', className='info-text')

# 3rd column
custom1_label = html.P('Custom 1:', className='info-text')
custom1_actual = html.P(id='node-custom1', className='info-text')

# 4th column
custom2_label = html.P('Custom 2:', className='info-text')
custom2_actual = html.P(id='node-custom2', className='info-text')

# 5td column
custom3_label = html.P('Custom 3:', className='info-text')
custom3_actual = html.P(id='node-custom3', className='info-text')

top_row = dbc.Row([dbc.Col(node_label), dbc.Col(weight_label),
                   dbc.Col(custom1_label), dbc.Col(custom2_label), dbc.Col(custom3_label)])

bottom_row = dbc.Row([dbc.Col(node_name), dbc.Col(weight_actual),
                      dbc.Col(custom1_actual), dbc.Col(custom2_actual), dbc.Col(custom3_actual)])

info_contents = html.Div([top_row, bottom_row])