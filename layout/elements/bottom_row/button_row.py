from dash import html
import dash_bootstrap_components as dbc

home_button = dbc.Button(
    id='home-button',
    children=html.I(className="fa-solid fa-house-chimney icon-style-bottom-row"),
    className="bottom-row-button",
    style={'outline': 'none'},
)

edit_button = dbc.Button(
    id='edit-button',
    children=html.I(className="fa-solid fa-wrench icon-style-bottom-row"),
    className="bottom-row-button",
)

button_row = dbc.Row([
    dbc.Col(home_button),
    dbc.Col(edit_button)
],
    style={'marginLeft': '50px'})
