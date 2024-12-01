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

custom1_label = html.P('CUSTOM 1', id='custom1_label', className='fields-label')
custom2_label = html.P('CUSTOM 2', id='custom2_label', className='fields-label')
custom3_label = html.P('CUSTOM 3', id='custom3_label', className='fields-label')

fields_store = dcc.Store(id='fields-store')

fields_body = html.Div(id='field_names_view',
                       children=[
                           html.Div(style={'height': '0vh'}),
                           dbc.Row(dbc.Col(custom1_label)),
                           dbc.Row([
                               dbc.Col(width=1),
                               dbc.Col(dbc.Input(id='custom1_input', className='weights-input',
                                                 style={'height':'8vh'})),
                               dbc.Col(width=1)
                           ]),
                           html.Div(style={'height': '1vh'}),
                           dbc.Row(dbc.Col(custom2_label), justify='center'),
                           dbc.Row([
                               dbc.Col(width=1),
                               dbc.Col(dbc.Input(id='custom2_input', className='weights-input',
                                                 style={'height':'8vh'})),
                               dbc.Col(width=1)
                           ]),
                           html.Div(style={'height': '1vh'}),
                           dbc.Row(dbc.Col(custom3_label)),
                           html.Div(style={'height': '1vh'}),
                           dbc.Row([
                               dbc.Col(width=1),
                               dbc.Col(dbc.Input(id='custom3_input', className='weights-input',
                                                 style={'height':'8vh'})),
                               dbc.Col(width=1),
                           ])
                       ])

field_names_store = dcc.Store(id='field-names-store', data=['', '', ''])

custom_fields = html.Div([
    fields_store,
    field_names_store,
    dbc.Row(custom_fields_title),
    html.Div(style={'height': '1vh'}),
    dbc.Row([dbc.Col(width=1), dbc.Col(field_names_button),
             dbc.Col(field_values_button)]
            ),
    html.Div(style={'height': '2vh'}),
    html.Div(fields_body),
    html.Div(style={'height': '3vh'}),
    dbc.Row([dbc.Col(width=4), dbc.Col(custom_update_button), dbc.Col(width=4)])

])
