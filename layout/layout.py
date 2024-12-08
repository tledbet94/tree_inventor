from dash import dcc, html
import dash_bootstrap_components as dbc

# internal imports
from .elements.panels import button_panel, control_panel, info_panel
from cytoscape.cytoscape import cyto_component, file_info

from .elements.control_panel.modes.home import home
from .elements.control_panel.modes.edit import edit
from .elements.control_panel.modes.edit import edit_input_button
from .elements.control_panel.modes.edit import edit_input
from .elements.control_panel.modes.edit import remove_node_button
from .elements.control_panel.modes.weights import weights
from .elements.control_panel.modes.custom_fields import custom_fields
from .elements.control_panel.modes.save_load import save_load
from .elements.control_panel.modes.themes import themes
from .elements.control_panel.modes.user import user
from .elements.control_panel.modes.settings import settings

name_dict = {
    'Starter Tree': 1,
    'Coin Flip': 2,
    'Game on the Line': 3,
    'Wake Up': 4,
    'Chess Openings': 5,
    'Stock Tree': 6,
    'Best Picture by Year': 7,
    'Wives of Henry VIII': 8
}

name = file_info['name']
starting_number = name_dict[name]

file_info = dcc.Store(id='file-info', data=file_info)

layout = html.Div([
    # separate elements copy for each function
    file_info,
    html.Div("Please rotate your device to landscape mode.", id='rotate-device-message'),
    dcc.Store('starting-template-number', data=starting_number),
    dcc.Store(id='edit-store'),
    dcc.Store(id='single-interval-store'),
    dcc.Store(id='multiple-interval-store'),
    dcc.Store(id='weights-store'),
    # other stores
    dcc.Store(id='current-node-data'),
    dcc.Interval(id='traversal-interval', interval=1000, n_intervals=0, disabled=True),
    dcc.Store(id='traversal-state'),
    dcc.Store(id='traversal-path'),
    dcc.Store(id='current-step'),
    # To assist with proper updating of selected node's name
    dcc.Store(id='name-store', data=''),
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
