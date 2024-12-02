from dash import dcc, html
import dash_bootstrap_components as dbc
import random

templates_title = html.H1('Templates', className='edit-header-text')

template_one = html.Div(
    children=[
        dbc.Button(id='template_one_button',
                   children="ONE",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_two = html.Div(
    children=[
        dbc.Button(id='template_two_button',
                   children="TWO",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_three = html.Div(
    children=[
        dbc.Button(id='template_three_button',
                   children="THREE",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_four = html.Div(
    children=[
        dbc.Button(id='template_four_button',
                   children="FOUR",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_five = html.Div(
    children=[
        dbc.Button(id='template_five_button',
                   children="FIVE",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_six = html.Div(
    children=[
        dbc.Button(id='template_six_button',
                   children="SIX",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_seven = html.Div(
    children=[
        dbc.Button(id='template_seven_button',
                   children="SEVEN",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_eight = html.Div(
    children=[
        dbc.Button(id='template_eight_button',
                   children="EIGHT",
                   className='template-button',
                   active=False
                   )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

template_store = dcc.Store(id='template-store')

random_number = 1
current_tree = dcc.Store(id='current-tree', data=random_number)

templates = html.Div([
    current_tree,
    template_store,
    templates_title,
    html.Div(style={'height': '8vh'}),
    dbc.Row([dbc.Col(template_one), dbc.Col(template_two)]),
    html.Div(style={'height': '12vh'}),
    dbc.Row([dbc.Col(template_three), dbc.Col(template_four)]),
    html.Div(style={'height': '12vh'}),
    dbc.Row([dbc.Col(template_five), dbc.Col(template_six)]),
    html.Div(style={'height': '12vh'}),
    dbc.Row([dbc.Col(template_seven), dbc.Col(template_eight)])
])
