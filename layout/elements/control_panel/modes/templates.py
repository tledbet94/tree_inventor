from dash import html
import dash_bootstrap_components as dbc

templates_title = html.H1('Templates', className='edit-header-text')

template_one = html.Div(
    children=[
        dbc.Button(id='template_one_button',
                   children="ONE",
                   className='template_button',
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
                   className='template_button',
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
                   className='template_button',
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
                   className='template_button',
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
                   className='template_button',
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
                   className='template_button',
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
                   className='template_button',
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
                   className='template_button',
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

templates = html.Div([
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
