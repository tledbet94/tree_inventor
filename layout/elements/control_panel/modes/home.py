from dash import dcc, html
import dash_bootstrap_components as dbc

# components to this mode

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Decision Tree", className="card-title"),
            html.Pre(
                "\nThis is a default cytoscape. This text can provide a description of your cytoscape, and you can "
                "later write your own text in this space as a cytoscape inventor.\n\n"
                "The current default cytoscape illustrates a decision cytoscape; note the "
                "weights tying decisions together and the sequential order of decisions.",
                className="card-text",
                style={
                    'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                    'overflow': 'hidden',  # Prevents the scrollbar from appearing
                    'font-size': '1vw'
                }
            ),
        ], className='home-card'
    ), className='home-card',
)

book_modal = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Resources"), close_button=True,
                                className='book-modal-header'),
                dbc.ModalBody(children=html.A('Wikipedia',
                                              href='https://en.wikipedia.org/wiki/Directed_acyclic_graph'),
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
            style={'outline': 'none', 'marginTop': '20px'},
            n_clicks=0)

# this gets exported

home = dbc.Container([
    dbc.Row(
        dbc.Col(
            card,
            width={"xs": 12, "sm": 10, "md": 8, "lg": 6, "xl": 4},
            className="mb-2"
        ),
        justify="center",
    ),
    dbc.Row([
        dbc.Col(width=4),
        dbc.Col([book_button, book_modal]),
        dbc.Col(width=4)
    ])
],
    fluid=True,
)