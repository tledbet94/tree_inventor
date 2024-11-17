from dash import dcc, html

# Internal imports
from .bottom_row.button_row import button_row
# For control panel
from .control_panel.modes.home import home
from .control_panel.modes.save_load import save_load
from .control_panel.modes.edit import edit
from .control_panel.modes.algorithims import algo
from .control_panel.modes.weights import weights
from .control_panel.modes.custom_fields import custom_fields
from .control_panel.modes.templates import templates
from .control_panel.modes.themes import themes
from .control_panel.modes.user import user
from .control_panel.modes.settings import settings

# For info panel
from .info_panel.info_components import info_contents

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
        html.Div(user, id='themes-mode', style={'display': 'none'}),
        html.Div(user, id='user-mode', style={'display': 'none'}),
        html.Div(settings, id='settings-mode', style={'display': 'none'})
    ],
    style={
        'height': '90vh',
        'padding': '10px'
    },
    className="menu-div"
)

info_panel = html.Div(
    children=[
        dcc.Store(id='info-panel-data'),
        info_contents,
    ],
    style={
        'height': '22vh',
        'padding': '10px'
    },
    className="info-div"
)

button_panel = html.Div(
    children=[
        button_row,
    ],
    style={
        'height': '100%',
        'padding': '10px',
        'display': 'flex',
        'justify-content': 'left',  # Centers horizontally
        'align-items': 'center'  # Centers vertically
    },
    className="menu-div"
)
