from dash import dcc, html
import dash_bootstrap_components as dbc

custom_fields_title = html.H1('CUSTOM FIELDS', className='edit-header-text')

field_names_button = dbc.Button(
    id='field-names-button',
    children="FIELD NAMES",
    className="fields-button",
    style={'outline': 'none', 'margin_left': '15px'},
    active=True
)

field_values_button = dbc.Button(
    id='field-values-button',
    children="VALUES",
    className="fields-button",
    style={'outline': 'none', 'margin_left': '15px'},
    active=False
)

custom_update_button = dbc.Button(
    id='custom-update-button',
    children="UPDATE",
    className="fields-update-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

custom1_label = html.H2('CUSTOM 1', id='custom1_label')
custom2_label = html.H2('CUSTOM 2', id='custom2_label')
custom3_label = html.H2('CUSTOM 3', id='custom3_label')

fields_store = dcc.Store(id='fields-store')

fields_body = html.Div(id='field_names_view',
                       children=[
                           dbc.Row([
                               dbc.Col(width=1), dbc.Col(html.H1('FROM')), dbc.Col(width=1),
                               dbc.Col(html.H1('TO')), dbc.Col(width=1),
                           ]),
                           html.Div(style={'height': '2vh'}),
                           dbc.Row([
                               dbc.Col(width=1), dbc.Col(custom1_label),
                               dbc.Col(width=1),
                               dbc.Col(dbc.Input(id='custom1_input')), dbc.Col(width=1),
                           ]),
                           html.Div(style={'height': '2vh'}),
                           dbc.Row([
                               dbc.Col(width=1), dbc.Col(custom2_label),
                               dbc.Col(width=1),
                               dbc.Col(dbc.Input(id='custom2_input')), dbc.Col(width=1),
                           ]),
                           html.Div(style={'height': '2vh'}),
                           dbc.Row([
                               dbc.Col(width=1), dbc.Col(custom3_label),
                               dbc.Col(width=1),
                               dbc.Col(dbc.Input(id='custom3_input')), dbc.Col(width=1),
                           ])
                       ])

custom_fields = html.Div([
    fields_store,
    dbc.Row(custom_fields_title),
    html.Div(style={'height': '1vh'}),
    dbc.Row([dbc.Col(field_names_button),
             dbc.Col(field_values_button)]
            ),
    html.Div(style={'height': '3vh'}),
    html.Div(fields_body),
    html.Div(style={'height': '1vh'}),
    dbc.Row([dbc.Col(width=3), dbc.Col(custom_update_button), dbc.Col(width=3)])

])
