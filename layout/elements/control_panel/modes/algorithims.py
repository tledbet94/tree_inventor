from dash import dcc, html
import dash_bootstrap_components as dbc

algo_title = html.H1('ALGORITHIMS', className='edit-header-text')

single_traversal_button = dbc.Button(
    id='single-traversal-button',
    children="SINGLE TRAVERSAL",
    className="algo-button",
)

traversal_output_display = html.Div(
    children=[
        html.Div(id='traversal-output-display',
                 children="",
                 className='algo-output-passive'
                 )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "5vh",
        "backgroundColor": "#b8b5b9"
    }
)

multiple_traversal_button = dbc.Button(
    id='multiple-traversal-button',
    children="MULTIPLE TRAVERSAL",
    className="algo-button",
)

interval_component = dcc.Interval(
    id='display-toggle-interval',
    interval=2000,  # 1.2 seconds to allow opacity transition to complete
    n_intervals=0,
    disabled=True
)

slider = html.Div([
    dcc.Slider(0, 6,
               id='algo-slider',
               marks={i: '{}'.format(10 ** i) for i in range(7)},
               value=2,
               updatemode='drag',
               step=None,
               className='algo-slider'
               ),
    html.Div(style={"height": "3vh"}),
    html.H3(id='algo-slider-text', children='', className='algo-slider-text')
])

spinner = html.Div(id='algo-spinner',
                   children=[dbc.Spinner(color='#4b80ca',
                                         spinner_style={"width": "4vh", "height": "4vh"})],
                   style={'textAlign': 'center', 'display': 'none'})


algo = dbc.Container([
    interval_component,
    dcc.Store(id='terminal-node-info', data={}),
    dbc.Row(
        dbc.Col(
            algo_title
        ),
        justify="center",
    ),
    html.Div(style={"height": "2vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(single_traversal_button, align='center'),
        dbc.Col(width=2)
    ], justify='center'),
    html.Div(style={"height": "12vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(
            children=[
                traversal_output_display,
            ],
            align='center',
        ),
        dbc.Col(width=1)
    ]),
    html.Div(style={"height": "12vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(multiple_traversal_button, align='center'),
        dbc.Col(width=2)
    ], justify='center'),
    html.Div(style={"height": "4vh"}),
    dbc.Row(slider),
    html.Div(style={"height": "1vh"}),
    dbc.Row(spinner)
],
    fluid=True,
)
