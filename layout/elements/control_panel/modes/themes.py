from dash import dcc, Input, html, Output
import dash_bootstrap_components as dbc
from app_instance import app

themes_title = html.H1('Themes', className='edit-header-text')

# Color
banana_button = dbc.Button(
    id='banana-button',
    children="B",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

grape_button = dbc.Button(
    id='grape-button',
    children="G",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

orange_button = dbc.Button(
    id='orange-button',
    children="O",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

# Node shape button
triangle_button = dbc.Button(
    id='triangle-button',
    children="TR",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

square_button = dbc.Button(
    id='square-button',
    children="SQ",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

octagon_button = dbc.Button(
    id='O-button',
    children="OC",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

# Node Outline button

no_outline_button = dbc.Button(
    id='no-outline-button',
    children="NOO",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

shadow_outline_button = dbc.Button(
    id='shadow-button',
    children="SHD",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
),

double_outline_button = dbc.Button(
    id='double-button',
    children="DOU",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

# Edge pointer

no_pointer_button = dbc.Button(
    id='no-pointer-button',
    children="NOPO",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

arrow_pointer_button = dbc.Button(
    id='arrow-pointer-button',
    children="ARRP",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

tee_pointer_button = dbc.Button(
    id='tee-pointer-button',
    children="TEPE",
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

themes_div = html.Div(children='test', className='themes-div')

themes = html.Div(
    [
        themes_title,
        html.Div(style={'height': '5vw'}),
        themes_div,
        html.Div(style={'height': '5vw'}),
        themes_div,
        html.Div(style={'height': '5vw'}),
        themes_div

    ]
)
