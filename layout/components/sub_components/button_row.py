from dash import html
import dash_bootstrap_components as dbc

button_row = dbc.Row([
        dbc.Button(
            html.I(className="bi bi-house icon-style"),  # Replace "bi bi-house" with the desired icon class
            className="btn-clean",
        ),
], style={'marginLeft': '50px'})
