from dash import html

# Internal imports
from .sub_components.info_components import info_contents
from .sub_components.button_row import button_row

control_panel = html.Div(
    children=[
        html.H1("Controls"),
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
