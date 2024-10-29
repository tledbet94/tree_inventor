from dash import html
import dash_bootstrap_components as dbc

button_row = dbc.Row([
        dbc.Button(
            id='home-button',
            children=html.I(className="bi bi-house icon-style"),  # Replace "bi bi-house" with the desired icon class
            className="btn-clean",
            style={'outline': 'none'},
            n_clicks=1
        ),
], style={'marginLeft': '50px'})

