from dash import html
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

field_update_button = dbc.Button(
    id='field-update-button',
    children="UPDATE",
    className="fields-update-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

field_names_body = html.Div(id='field_names_view',
                            children=[
                                dbc.Row([
                                    dbc.Col(width=1), dbc.Col(html.H1('FROM')), dbc.Col(width=1),
                                    dbc.Col(html.H1('TO')), dbc.Col(width=1),
                                ]),
                                html.Div(style={'height': '4vh'}),
                                dbc.Row([
                                    dbc.Col(width=1), dbc.Col(html.H2('CUSTOM 1')), dbc.Col(width=1),
                                    dbc.Col(dbc.Input()), dbc.Col(width=1),
                                ]),
                                html.Div(style={'height': '3vh'}),
                                dbc.Row([
                                    dbc.Col(width=1), dbc.Col(html.H2('CUSTOM 2')), dbc.Col(width=1),
                                    dbc.Col(dbc.Input()), dbc.Col(width=1),
                                ]),
                                html.Div(style={'height': '3vh'}),
                                dbc.Row([
                                    dbc.Col(width=1), dbc.Col(html.H2('CUSTOM 3')), dbc.Col(width=1),
                                    dbc.Col(dbc.Input()), dbc.Col(width=1),
                                ]),
                                html.Div(style={'height': '5vh'}),
                                dbc.Row([dbc.Col(width=3), dbc.Col(field_update_button), dbc.Col(width=3)])

                            ],
                            style={'display': 'block'}
                            )

field_values_body = html.Div(id='field_values_view',
                             children=[
                                 dbc.Row([
                                     dbc.Col(width=1), dbc.Col(html.H1('FROM')), dbc.Col(width=1),
                                     dbc.Col(html.H1('TO')), dbc.Col(width=1),
                                 ]),
                                 html.Div(style={'height': '4vh'}),
                                 dbc.Row([
                                     dbc.Col(width=1), dbc.Col(html.H2('CUSTOM 1')), dbc.Col(width=1),
                                     dbc.Col(dbc.Input()), dbc.Col(width=1),
                                 ]),
                                 html.Div(style={'height': '3vh'}),
                                 dbc.Row([
                                     dbc.Col(width=1), dbc.Col(html.H2('CUSTOM 2')), dbc.Col(width=1),
                                     dbc.Col(dbc.Input()), dbc.Col(width=1),
                                 ]),
                                 html.Div(style={'height': '3vh'}),
                                 dbc.Row([
                                     dbc.Col(width=1), dbc.Col(html.H2('CUSTOM 3')), dbc.Col(width=1),
                                     dbc.Col(dbc.Input()), dbc.Col(width=1),
                                 ]),
                                 html.Div(style={'height': '5vh'}),
                                 dbc.Row([dbc.Col(width=3), dbc.Col(field_update_button), dbc.Col(width=3)])

                             ],
                             style={'display': 'none'}
                             )


custom_fields = html.Div([
    dbc.Row(custom_fields_title),
    html.Div(style={'height': '5vh'}),
    dbc.Row([dbc.Col(field_names_button),
             dbc.Col(field_values_button)]
            ),
    html.Div(style={'height': '5vh'}),
    html.Div([field_names_body, field_values_body])

])
