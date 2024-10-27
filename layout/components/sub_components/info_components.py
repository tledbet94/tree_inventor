from dash import html
import dash_bootstrap_components as dbc

# 1st column
node_label = html.P('Element', className='info-text')
node_name = html.P(id='node-name', className='info-text')

# 2nd column
parent_label = html.P('Weight', className='info-text')
parent_name = html.P(id='node-weight', className='info-text')

top_row = dbc.Row([dbc.Col(node_label), dbc.Col(parent_label)])
bottom_row = dbc.Row([node_name, parent_name])

info_contents = html.Div([top_row, bottom_row])