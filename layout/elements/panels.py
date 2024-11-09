from dash import html

# Internal imports
from .bottom_row.button_row import button_row
# For control panel
from .control_panel.modes.home import home
from .control_panel.modes.edit import edit
from .control_panel.modes.algorithims import algo
# For info panel
from .info_panel.info_components import info_contents

control_panel = html.Div(
    id='control-panel',
    children=[
        html.Div(home, id='home-mode', style={'display': 'block'}),
        html.Div(edit, id='edit-mode', style={'display': 'none'}),
        html.Div(algo, id='algo-mode', style={'display': 'none'}),
    ],
    style={
        'height': '90vh',
        'padding': '10px'
    },
    className="menu-div"
)


info_panel = html.Div(
    children=[
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
