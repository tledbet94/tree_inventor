from dash import dcc, html
import dash_bootstrap_components as dbc

home_button = dbc.Button(
    id='home-button',
    children=html.I(className="fa-solid fa-house-chimney icon-style-bottom-row"),
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False,
)

save_load_button = dbc.Button(
    id='save-load-button',
    children=html.I(className="fa-solid fa-floppy-disk icon-style-bottom-row"),
    className="bottom-row-button",
    style={'outline': 'none'},
    disabled=False
)

edit_button = dbc.Button(
    id='edit-button',
    children=html.I(className="fa-solid fa-wrench icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

algo_button = dbc.Button(  # Removed trailing comma here
    id='algo-button',
    children=html.I(className="fa-solid fa-shuffle icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

weights_button = dbc.Button(  # Removed trailing comma here
    id='weights-button',
    children=html.I(className="fa-solid fa-scale-balanced icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

custom_fields_button = dbc.Button(
    id='custom-fields-button',
    children=html.I(className="fa-solid fa-scroll icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

templates_button = dbc.Button(
    id='templates-button',
    children=html.I(className="fa-solid fa-parachute-box icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

theme_button = dbc.Button(
    id='themes-button',
    children=html.I(className="fa-solid fa-brush icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

user_button = dbc.Button(
    id='user-button',
    children=html.I(className="fa-solid fa-user icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

settings_button = dbc.Button(
    id='settings-button',
    children=html.I(className="fa-solid fa-gear icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

dummy_button = dbc.Button(
    children=html.I(className="fa-solid fa-diamond icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

dummy = dbc.Col(dummy_button, style={'opacity': 0})  # Removed trailing comma here

button_row = dbc.Row([
    dcc.Store(id='active-button-store', data='home'),
    # I want these buttons aligned to the left of the row
    dbc.Col(home_button),
    dbc.Col(save_load_button),
    html.Div(style={'width': '40vh'}),
    # I want these buttons aligned to the middle of the row
    dbc.Col(edit_button),
    dbc.Col(algo_button),
    dbc.Col(weights_button),
    dbc.Col(custom_fields_button),
    # I want these buttons aligned to the right of the row
    html.Div(style={'width': '15vh'}),
    dbc.Col(templates_button),
    dbc.Col(theme_button),
    dbc.Col(user_button),
    dbc.Col(settings_button),
], style={'marginLeft': '50px'})
