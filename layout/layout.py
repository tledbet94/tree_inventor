from dash import dcc, html, Input, Output, State, callback, clientside_callback
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

# internal imports
from .elements.panels import button_panel, control_panel, info_panel
from cytoscape.cytoscape import cyto_component, file_info

from .elements.control_panel.modes.home import home
from .elements.control_panel.modes.edit import edit, edit_input_button, edit_input, remove_node_button
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

# Orientation detection: Store and Interval
orientation_store = dcc.Store(id='orientation-store')
orientation_check = dcc.Interval(id='orientation-check', interval=1000, n_intervals=0)

change_screen = dbc.Button(children='SWITCH VIEW', id='change-view-button', className='switch-button')

layout = html.Div([
    file_info,
    orientation_store,
    orientation_check,
    dcc.Store('starting-template-number', data=starting_number),
    dcc.Store(id='edit-store'),
    dcc.Store(id='single-interval-store'),
    dcc.Store(id='multiple-interval-store'),
    dcc.Store(id='weights-store'),
    dcc.Store(id='current-node-data'),
    dcc.Interval(id='traversal-interval', interval=1000, n_intervals=0, disabled=True),
    dcc.Store(id='traversal-state'),
    dcc.Store(id='traversal-path'),
    dcc.Store(id='current-step'),
    dcc.Store(id='name-store', data=''),

    dbc.Row([dbc.Col(width=11), dbc.Col(change_screen)], className='top-div', style={'position': 'relative'}),

    dbc.Row([
        dbc.Col(
            control_panel,
            width=3,
            id='control-col',
            style={'padding': '0', 'height': '100%'}
        ),
        dbc.Col([
            cyto_component,
            info_panel,
        ],
            width=9,
            id='cyto-col',
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

# Cytoscape background and styling for reference
cytoscape_background_color = '#352b42'

# Client-side callback to detect orientation
# Returns 'landscape' if width > height, else 'portrait'
# This runs in the browser and updates the orientation-store
clientside_callback(
    """
    function(n) {
        const isLandscape = window.innerWidth > window.innerHeight;
        return isLandscape ? 'landscape' : 'portrait';
    }
    """,
    Output('orientation-store', 'data'),
    Input('orientation-check', 'n_intervals')
)
