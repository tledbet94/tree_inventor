from dash import html
import dash_bootstrap_components as dbc

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Decision Tree", className="card-title"),
            html.H6("Is loaded", className="card-subtitle"),
            html.Pre(
                "\nThis is a default tree. This text can provide a description of your tree, and you can "
                "later write your own text in this space as a tree inventor.\n\n"
                "The current default tree illustrates a decision tree; note the "
                "weights tying decisions together and the sequential order of decisions."
                "\n\n"
                "This app is configured to build Directed Acyclic Graphs (DAG) - a particular style of tree. More"
                " information can be found in the resources link below. Additionally the trees created in this "
                "application can be described as General Trees, which are connected trees with n nodes, n-1 edges"
                ", and no cycles.\n\nThe goal of tree inventor is to provide a platform to visualize data structures"
                " and/or create them, using this type of graph/tree across its varied use cases.  ",
                className="card-text",
                style={
                    'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                    'overflow': 'hidden',  # Prevents the scrollbar from appearing
                    'font-size': '16px'
                }
            ),
            html.H6("Author: "),
            html.P("Thomas Ledbetter"),
        ], className='clean-card'
    ), className='clean-card',
    style={"width": "30rem", 'height': '50rem'},
)

resources_button = dbc.Button(
            id='resources-button',
            children=html.I(className="fa-solid fa-book icon-style-alt"),
            className="btn-clean-alt",
            style={'outline': 'none', 'marginTop': '20px'},
            n_clicks=1)

home = html.Div([card,
                 html.Div(
                     resources_button,
                     style={
                         'display': 'flex',
                         'justify-content': 'center',  # Horizontal centering
                         'align-items': 'center',  # Vertical centering
                     }
                 )
                 ])