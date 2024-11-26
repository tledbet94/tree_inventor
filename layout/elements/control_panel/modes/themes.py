from dash import dcc, Input, html, Output
import dash_bootstrap_components as dbc
from app_instance import app

themes_title = html.H1('Themes', className='edit-header-text')

dropdown = dbc.DropdownMenu(
    label="Choose ",
    children=[
        dbc.DropdownMenuItem("Item 1"),
        dbc.DropdownMenuItem("Item 2"),
        dbc.DropdownMenuItem("Item 3"),
    ], style={'marginLeft': '2.5vw'}
)

colorpicker_text = html.Div(html.P(children="Select a color below.", className="theme-font"),
                            style={'textAlign': 'center'})

colorpicker = html.Div(
    dbc.Input(
        type="color",
        id="colorpicker",
        value="#4b80ca",
        className="colorpicker-input",
    ),
    className="colorpicker-container",
)

apply_button = dbc.Button(children='Apply', id='themes-apply-button', className='themes-apply-button')

presets_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Preset Themes"), close_button=True,
                        className='book-modal-header'),
        dbc.ModalBody(children=html.A('Wikipedia',
                                      href='https://en.wikipedia.org/wiki/Directed_acyclic_graph'),
                      className='presets-modal-body'),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="presets-modal-close-button",
                className="modal-button",
                n_clicks=0
            ), className='presets-modal-footer'
        ),
    ],
    id="presets-modal",
    centered=True,
    is_open=False,
)

presets_button = dbc.Button(
    id='presets-button',
    children=('PRESETS'),
    className="themes-apply-button",
    style={'outline': 'none'},
    n_clicks=0)

themes = html.Div(
    [
        themes_title,
        html.Div(style={'height': '4vh'}),
        dropdown,
        html.Div(style={'height': '14vh'}),
        colorpicker_text,
        html.Div(style={'height': '8vh'}),
        dbc.Row([dbc.Col(width=2), dbc.Col(colorpicker), dbc.Col(apply_button), dbc.Col(width=2)]),
        html.Div(style={'height': '8vh'}),
        dbc.Row(
            [
                dbc.Col(width=4),
                dbc.Col([presets_button, presets_modal]),
                dbc.Col(width=4)
                 ]
        )

    ]
)
