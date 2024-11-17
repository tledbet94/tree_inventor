from dash import html
import dash_bootstrap_components as dbc

custom_fields_title = html.H1('CUSTOM FIELDS', className='edit-header-text')

field_names_button = dbc.Button(
    id='field-names-button',
    children="FIELD NAMES",
    className="fields-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

field_values_button = dbc.Button(
    id='field-values-button',
    children="VALUES",
    className="fields-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

custom_fields = html.Div([
    dbc.Row(custom_fields_title),
    html.Div(style={'height': '5vh'}),
    dbc.Row([dbc.Col(field_names_button),
             dbc.Col(field_values_button)]
            )])
