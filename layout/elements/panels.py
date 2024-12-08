from dash import dcc, html
# Internal imports
from .bottom_row.button_row import button_row
from .control_panel.modes.home import home
from .control_panel.modes.save_load import save_load
from .control_panel.modes.edit import edit
from .control_panel.modes.traversal import algo
from .control_panel.modes.weights import weights
from .control_panel.modes.custom_fields import custom_fields
from .control_panel.modes.templates import templates
from .control_panel.modes.themes import themes
from .control_panel.modes.user import user
from .control_panel.modes.settings import settings

from .info_panel.info_components import info_contents

import dash_bootstrap_components as dbc

control_panel = html.Div(
    id='control-panel',
    children=[
        html.Div(home, id='home-mode', style={'display': 'block'}),
        html.Div(save_load, id='save-load-mode', style={'display': 'none'}),
        html.Div(edit, id='edit-mode', style={'display': 'none'}),
        html.Div(algo, id='algo-mode', style={'display': 'none'}),
        html.Div(weights, id='weights-mode', style={'display': 'none'}),
        html.Div(custom_fields, id='custom-fields-mode', style={'display': 'none'}),
        html.Div(templates, id='templates-mode', style={'display': 'none'}),
        html.Div(themes, id='themes-mode', style={'display': 'none'}),
        html.Div(user, id='user-mode', style={'display': 'none'}),
        html.Div(settings, id='settings-mode', style={'display': 'none'})
    ],
    className="p-2 menu-div",  # Add some padding
    style={
        'height': 'auto',  # Remove fixed heights
        'overflowY': 'auto'  # Allow scroll if needed on small screens
    }
)

info_panel = html.Div(
    children=[
        dcc.Store(id='info-panel-data'),
        info_contents,
    ],
    className="p-2 info-div",
    style={
        'height': 'auto',  # Let it size naturally
        'overflowY': 'auto'  # Scrolling if needed
    }
)

button_panel = html.Div(
    children=[
        button_row,
    ],
    className="d-flex align-items-center p-2 menu-div",
    style={
        'width': '100%',
        'justify-content': 'flex-start',  # Align left
        'overflowX': 'auto'  # Allow horizontal scroll on small screens if needed
    }
)
