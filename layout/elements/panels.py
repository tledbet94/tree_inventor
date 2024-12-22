from dash import dcc, html
import dash_bootstrap_components as dbc

# Internal imports
from .bottom_row.button_row import button_row
# For control panel
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

from .control_panel.modes.ai import ai

# For info panel
from .info_panel.info_components import info_contents

control_panel = dbc.Container(
    id='control-panel',
    children=[
        dbc.Container(home, id='home-mode', style={'display': 'block'}, fluid=True),
        dbc.Container(save_load, id='save-load-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(edit, id='edit-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(algo, id='algo-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(weights, id='weights-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(custom_fields, id='custom-fields-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(templates, id='templates-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(themes, id='themes-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(user, id='user-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(settings, id='settings-mode', style={'display': 'none'}, fluid=True),
        dbc.Container(ai, id='ai-mode', style={'display': 'none'}, fluid=True)
    ], fluid=True,
    className="control-div"
)

info_panel = info_contents

button_panel = button_row
