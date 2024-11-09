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
        dbc.Col(width=1),
        dbc.Col(single_traversal_button, align='center'),
        dbc.Col(width=1)
    ], justify='center'),
    html.Div(style={"height": "16vh"}),
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
    html.Div(style={"height": "16vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(multiple_traversal_button, align='center'),
        dbc.Col(width=1)
    ], justify='center')
],
    fluid=True,
)
