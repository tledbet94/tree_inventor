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
    html.Div(style={'height': '5vh'}),

    # First Row
    dbc.Row(
        [
            dbc.Col(template_one, width=6),  # Adjust column width if needed
            dbc.Col(template_two, width=6)
        ],
        justify="center",  # Optional: aligns columns in the center
        className="flex-nowrap no-gutters"
    ),
    html.Div(style={'height': '12vh'}),

    # Second Row
    dbc.Row(
        [
            dbc.Col(template_three, width=6),
            dbc.Col(template_four, width=6)
        ],
        justify="center",
        className="flex-nowrap no-gutters"
    ),
    html.Div(style={'height': '12vh'}),
    # Third Row
    dbc.Row(

        [
            dbc.Col(template_five, width=6),
            dbc.Col(template_six, width=6)
        ],
        justify="center",
        className="flex-nowrap no-gutters"
    ),
    html.Div(style={'height': '12vh'}),

    # Fourth Row
    dbc.Row(
        [
            dbc.Col(template_seven, width=6),
            dbc.Col(template_eight, width=6)
        ],
        justify="center",
        className="flex-nowrap no-gutters"
    )
])
