from dash import dcc, Input, html, Output
import dash_bootstrap_components as dbc
from app_instance import app

themes_title = html.H1('Themes', className='edit-header-text')

dropdown = dbc.DropdownMenu(
    label="Menu",
    children=[
        dbc.DropdownMenuItem("Item 1"),
        dbc.DropdownMenuItem("Item 2"),
        dbc.DropdownMenuItem("Item 3"),
    ],
)

colorpicker = html.Div(
    [
        html.P(children="Select a color below.", className="theme-font"),
        dbc.Input(
            type="color",
            id="colorpicker",
            value="#4b80ca",
            className="colorpicker-input",
        ),
    ],
    className="colorpicker-container",
)

themes = html.Div(
    [
        themes_title,
        html.Div(style={'height': '12vh'}),
        colorpicker
    ]
)
