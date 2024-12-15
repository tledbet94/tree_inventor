from dash import html
import dash_bootstrap_components as dbc

objective_paragraph = ("Build Trees!. Weights and custom fields are "
                       " in each tree. There many customization possibilities, "
                       "and you can save (load) to (from) JSON.")

credits_paragraph = ("Built using Dash Cytoscape; extends Cytoscape.js; extends "
                     "Cytoscape.js-dagre. Check out the book button in home.")

user_card = dbc.Card(
    dbc.CardBody(
        [
            html.Div(style={'height': '5vh'}),
            html.Pre(children=objective_paragraph,
                     className="card-text",
                     style={
                         'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                         'overflow': 'hidden',  # Prevents the scrollbar from appearing
                         'font-size': '1vw'
                     }
                     ),
            html.Pre(children=credits_paragraph,
                     className="card-text",
                     style={
                         'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                         'overflow': 'hidden',  # Prevents the scrollbar from appearing
                         'font-size': '1vw'
                     }
                     ),
            dbc.Row([
                html.A('GitHub', className="sleek-link",
                       href='https://github.com/tledbet94'),
                html.A('LinkedIn', className="sleek-link",
                       href='https://www.linkedin.com/in/thomas-ledbetter-cfa%C2%AE-a4bb47120/')
            ])
        ], className='home-card'
    ), className='home-card',
)

user = html.Div([
    user_card
])
