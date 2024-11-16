from dash import dcc, html
import dash_bootstrap_components as dbc

home_button = dbc.Button(
    id='home-button',
    children=html.I(className="fa-solid fa-house-chimney icon-style-bottom-row"),
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,  # Add this line
)

edit_button = dbc.Button(
    id='edit-button',
    children=html.I(className="fa-solid fa-wrench icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,  # Add this line
)

algo_button = dbc.Button(
    id='algo-button',
    children=html.I(className="fa-solid fa-shuffle icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,  # Add this line
),

weights_button = dbc.Button(
    id='weights-button',
    children=html.I(className="fa-solid fa-scale-balanced icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,  # Add this line
)

custom_fields_button = dbc.Button(
    id='custom-fields-button',
    children=html.I(className="fa-solid fa-scroll icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,  # Add this line
)

templates_button = dbc.Button(
    id='templates-button',
    children=html.I(className="fa-solid fa-parachute-box icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,  # Add this line
)

button_row = dbc.Row([
    dcc.Store(id='active-button-store', data='home'),
    dbc.Col(home_button),
    dbc.Col(edit_button),
    dbc.Col(algo_button),
    dbc.Col(weights_button),
    dbc.Col(custom_fields_button),
    dbc.Col(templates_button)
], style={'marginLeft': '50px'})
