from dash import dcc, html
import dash_bootstrap_components as dbc

weights_title = html.H1('WEIGHTS', className='weights-header-text')

# Input components only appear when they are needed
weights_input_feedback = (
    html.Div(
        html.P('Placeholder', id='weights-input-feedback', className='weights-input-font'),
        className='input-feedback-div-weights'
    ))

weights_input = (
    dbc.Input(id='weights-input', placeholder='', size='lg', valid=False, className='weights-input'))

weights_input_button = (
    dbc.Button(id='weights-input-button', children='ENTER', className='hidden-opacity'))

weights = html.Div([
    dcc.Store(id='weights-enter-click-store', data=0),
    html.H1('MODIFY WEIGHTS', className='edit-header-text'),
    html.Div(style={"height": "8vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(weights_input_feedback),
        dbc.Col(width=1)
    ], id='weights-input-feedback-row', justify='center'),
    html.Div(style={"height": "3vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(weights_input, width=8),
        dbc.Col(weights_input_button, width=3),
    ], id='weights-input-row')
])
