from dash import html
import dash_bootstrap_components as dbc

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Decision Tree", className="card-title"),
            html.H6("Is loaded", className="card-subtitle"),
            html.P(
                "This is a default tree. This text can provide a description of your tree, and you can"
                " later create your own text in this space as a tree inventor."
                " The current default tree illustrates a decision tree; note the"
                " weights tying decisions together and the sequential order of decisions.",
                className="card-text",
            ),
            html.H6("Author: "),
            html.P("Thomas Ledbetter"),
        ], className='clean-card'
    ), className='clean-card',
    style={"width": "30rem"},
)

home = html.Div(card)