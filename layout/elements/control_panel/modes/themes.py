from dash import dcc, Input, html, Output
import dash_bootstrap_components as dbc
from app_instance import app

themes_title = html.H1('Themes', className='edit-header-text')

colorpicker = html.Div(
    [
        dbc.Label(["Select a ", html.Span("color", id="color", className='theme-font')], className="colorpicker-label"),
        html.Div(
            id="color-display",
            className="color-display",
            style={"background-color": "#000000"},  # Default color
        ),
        dbc.Input(
            type="color",
            id="colorpicker",
            value="#b8b5b9",
            className="colorpicker-input",
        ),
    ],
    className="colorpicker-container",
)

app.clientside_callback(
    """
    function(color) {
        document.getElementById('color-display').style.backgroundColor = color;
        return {};
    }
    """,
    Output("color", "style"),
    Input("colorpicker", "value"),
)

themes = html.Div(
    [
        themes_title,
        html.Div(style={'height': '12vh'}),
        colorpicker
    ]
)
