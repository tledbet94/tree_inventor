from dash import dcc, html
import dash_bootstrap_components as dbc

# components to this mode

card = dbc.Card(
    dbc.CardBody(
        [
            html.Div(style={'height': '6vh'}),
            html.P(id='card-title', className="card-title", style={'font-size': '1vw'}),
            html.P(id='card-author', className='card-text', style={'font-size': '1vw'}),
            html.Pre(id='card-description',
                     className="card-text",
                     style={
                         'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                         'overflow': 'hidden',  # Prevents the scrollbar from appearing
                         'font-size': '1vw'
                     }
                     ),
        ], className='home-card'
    ), className='home-card', style={'height': '55vh', 'width': '15vw'}
)

book_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Resources"), close_button=True,
                        className='book-modal-header'),
        dbc.ModalBody(children=[html.A('Wikipedia: DAG',
                                       href='https://en.wikipedia.org/wiki/Directed_acyclic_graph'),
                                html.P(''),
                                html.A('Cytoscape.js',
                                       href='https://js.cytoscape.org/'),
                                html.P(''),
                                html.A('Dash Cytoscape',
                                       href='https://dash.plotly.com/cytoscape'),
                                html.P(''),
                                html.A('cytoscape-dagre',
                                       href='https://github.com/cytoscape/cytoscape.js-dagre'),
                                ],
                      className='book-modal-body'),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="modal-close-button",
                className="modal-button",
                n_clicks=0
            ), className='book-modal-footer'
        ),
    ],
    id="book-modal",
    centered=True,
    is_open=False,
)

book_button = dbc.Button(
    id='book-button',
    children=html.I(className="fa-solid fa-book icon-style-book"),
    className="book-button",
    style={'outline': 'none', 'marginTop': '5vh'},
    n_clicks=0)

# this gets exported

home = dbc.Container(
    [
        dbc.Row(
            dbc.Col(card, width="auto"),
            className="d-flex justify-content-center align-items-center",
            style={"height": "50vh"}  # Give some vertical space to see the centering clearly
        ),
        html.Div(style={'height':'1vh'}),
        dbc.Row([
            dbc.Col(width=4),
            dbc.Col([book_button, book_modal]),
            dbc.Col(width=4)
        ])
    ]
)

