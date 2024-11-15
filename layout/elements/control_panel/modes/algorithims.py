from dash import dcc, html
import dash_bootstrap_components as dbc

algo_title = html.H1('ALGORITHMS', className='edit-header-text')

single_traversal_info = html.Div(
    [
        html.P(
            html.I(
                className="fa-solid fa-question icon-style-question-mark",
                id="st-tooltip-target",  # Add an ID for the tooltip target
                style={"cursor": "pointer", 'font-size': '6vh'},  # Optional: pointer cursor for better UX
            ),
        ),
        dbc.Tooltip(
            "A traversal will randomly select a node in the tree based on the weights assigned to nodes and "
            "edges. If a node's weight is above 0%, there is a % chance out of 100% that it is selected as the "
            "terminal node. If an edge's weight is above 0%, there is a % chance that the selected node will transfer"
            "to a child node based on that edge. The terminal node selected through traversal is returned. "
            "\n"
            "The color purple designates the traversal path. The node at the end of the path is the terminal node.",
            target="st-tooltip-target",  # Match this to the ID above
            className='algo-tooltip'
        ),
    ], style={
        "display": "flex",
        "justifyContent": "center",  # Center horizontally
        "alignItems": "flex-end",  # Align the <i> element to the bottom
        "height": "100px"  # Set the height of the container
    }
)

multiple_traversal_info = html.Div(
    [
        html.P(
            html.I(
                className="fa-solid fa-question icon-style-question-mark",
                id="mt-tooltip-target",  # Add an ID for the tooltip target
                style={"cursor": "pointer", 'font-size': '6vh'},  # Optional: pointer cursor for better UX
            ),
        ),
        dbc.Tooltip(
            "Run the selected number of (single) traversals, highlighting both the paths that have been "
            "traversed and the paths that have been the most traversed over the course of the simulation. The "
            "most frequent terminal node is returned.",
            target="mt-tooltip-target",  # Match this to the ID above
            className='algo-tooltip'
        ),
    ], style={
        "display": "flex",
        "justifyContent": "center",  # Center horizontally
        "alignItems": "flex-end",  # Align the <i> element to the bottom
        "height": "100px"  # Set the height of the container
    }
)

single_traversal_button = dbc.Button(
    id='single-traversal-button',
    children="SINGLE TRAVERSAL",
    className="algo-button",
    disabled=False,  # Add this line
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
    disabled=False,  # Add this line
)

interval_component = dcc.Interval(
    id='display-toggle-interval',
    interval=2000,
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
               className='algo-slider',
               disabled=False
               ),
    html.Div(style={"height": "3vh"}),
    html.H3(id='algo-slider-text', children='', className='algo-slider-text')
])

multiple_traversal_progress = dbc.Progress(
    value=0,
    id="multiple-traversal-progress",
    animated=False,
    striped=False,
    style={
        'display': 'none',
    },
    class_name='algo-progress',
    max=100,
    min=0
)

algo = dbc.Container([
    interval_component,
    dcc.Store(id='terminal-node-info', data={}),
    dcc.Interval(id='multiple-traversal-interval', interval=500, n_intervals=0, disabled=True),
    dcc.Store(id='multiple-traversal-state', data={}),
    dcc.Store(id='traversal-running', data=False),
    dbc.Row(
        dbc.Col(
            algo_title
        ),
        justify="center",
    ),
    html.Div(style={"height": "1vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(single_traversal_button, align='center'),
        dbc.Col(single_traversal_info, width=2)
    ], justify='center'),
    html.Div(style={"height": "13vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(
            children=[
                traversal_output_display,
            ],
            align='center',
        ),
        dbc.Col(width=1)
    ], justify='center'),
    html.Div(style={"height": "11vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(multiple_traversal_button, align='center'),
        dbc.Col(multiple_traversal_info, width=2)
    ], justify='center'),
    html.Div(style={"height": "1vh"}),
    dbc.Row(slider),
    html.Div(style={"height": "1vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(multiple_traversal_progress),
        dbc.Col(width=1)
    ]),
],
    fluid=True,
)
