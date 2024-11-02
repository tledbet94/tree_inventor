from dash import html
import dash_bootstrap_components as dbc

# internal imports
from .elements.panels import button_panel, control_panel, info_panel
from cytoscape.cytoscape import cyto_component

layout = html.Div([
    dbc.Row([
        dbc.Col(
            control_panel,
            width=3,
            style={'padding': '0', 'height': '100%'}
        ),
        dbc.Col([
            cyto_component,
            info_panel,
        ],
            width=9,
            style={'padding': '0', 'height': '100%'}
        )
    ],
        justify='start',
        style={'margin': '0', 'padding': '0', 'height': '100%'}),

    dbc.Row(
        dbc.Col(
            button_panel,
            width=12,
            style={'padding': '0', 'height': '10vh'}
        ),
        style={'margin': '0', 'padding': '0', 'height': '10vh'}
    )
],
    style={'margin': '0', 'padding': '0', 'height': '100%', 'overflow': 'hidden'}
)
