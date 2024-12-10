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
    children=html.I(className="fa-solid fa-info fa-2x"),
    className="bottom-row-button",
    disabled=False,
)

settings_button = dbc.Button(
    id='settings-button',
    children=html.I(className="fa-solid fa-gear icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
    style={'display': 'none'}
)

dummy_button = dbc.Button(
    children=html.I(className="fa-solid fa-diamond icon-style-bottom-row"),
    className="bottom-row-button",
    disabled=False,
)

dummy = dbc.Col(dummy_button, style={'opacity': 0})  # Removed trailing comma here
button_row = dbc.Row(
    [
        dcc.Store(id='buttons-store'),
        dcc.Store(id='active-button-store', data='home'),

        # Left-aligned buttons
        dbc.Col(
            [home_button, user_button, save_load_button],
            width="auto",
            className="d-flex justify-content-start align-items-center"
        ),

        # Spacer column for centering
        dbc.Col(
            width="auto",  # Flexible spacer
            className="flex-grow-1 d-none d-md-block"  # Visible only on medium+ screens
        ),

        # Center-aligned buttons
        dbc.Col(
            [edit_button, weights_button, custom_fields_button],
            width="auto",
            className="d-flex justify-content-center align-items-center"
        ),

        # Spacer column for right alignment
        dbc.Col(
            width="auto",
            className="flex-grow-1 d-none d-md-block"  # Visible only on medium+ screens
        ),

        # Right-aligned buttons
        dbc.Col(
            [algo_button, templates_button, theme_button, settings_button],
            width="auto",
            className="d-flex justify-content-end align-items-center"
        ),
    ],
    className="menu-div",  # Ensures vertical alignment across all buttons
    style={"flex-wrap": "nowrap", 'height': '10vh',
           'display': 'flex',
           'align-items': 'center'}  # Prevents buttons from wrapping to the next row
)
