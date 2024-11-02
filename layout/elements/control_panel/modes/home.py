from dash import dcc, html
import dash_bootstrap_components as dbc

# components to this mode

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Decision Tree", className="card-title"),
            html.H6("Is loaded", className="card-subtitle"),
            html.Pre(
                "\nThis is a default cytoscape. This text can provide a description of your cytoscape, and you can "
                "later write your own text in this space as a cytoscape inventor.\n\n"
                "The current default cytoscape illustrates a decision cytoscape; note the "
                "weights tying decisions together and the sequential order of decisions."
                "\n\n"
                "This app is configured to build Directed Acyclic Graphs (DAG) - a particular style of cytoscape. More"
                " information can be found in the resources link below. Additionally the trees created in this "
                "application can be described as General Trees, which are connected trees with n nodes, n-1 edges"
                ", and no cycles.\n\nThe goal of cytoscape inventor is to provide a platform to visualize data structures"
                " and/or create them, using this type of graph/cytoscape across its varied use cases.  ",
                className="card-text",
                style={
                    'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                    'overflow': 'hidden',  # Prevents the scrollbar from appearing
                    'font-size': '16px'
                }
            ),
            html.H6("Author: "),
            html.P("Thomas Ledbetter"),
        ], className='home-card'
    ), className='home-card',
    style={"width": "30rem", 'height': '50rem'},
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


book_button = html.Button(
            id='book-button',
            children=html.I(className="fa-solid fa-book icon-style-book"),
            className="book-button",
            style={'outline': 'none', 'marginTop': '20px'},
            n_clicks=0)

# this gets exported

home = html.Div([card,
                 html.Div([
                     book_button,
                     book_modal
                     ],
                     style={
                         'display': 'flex',
                         'justify-content': 'center',  # Horizontal centering
                         'align-items': 'center',  # Vertical centering
                     },
                 )
                 ])