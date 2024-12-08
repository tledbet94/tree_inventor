from dash import html
import dash_bootstrap_components as dbc

objective_paragraph = ("This is a platform to build trees. Weights and custom fields are "
                       "embedded in each tree. Tree traversal, template trees, "
                       "visual customization, and saving/loading in a JSON format are features. ")

credits_paragraph = ("This application was built using Dash Cytoscape which extends Cytoscape.js and "
                     "Cytoscape.js-dagre within. For more information see Resources in the home panel.")

user_card = dbc.Card(
    dbc.CardBody(
        [
            html.H2(children='ABOUT THIS APP', className="card-title"),
            html.H3(children='Objective', className="card-title"),
            html.Pre(children=objective_paragraph,
                     className="card-text",
                     style={
                         'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                         'overflow': 'hidden',  # Prevents the scrollbar from appearing
                         'font-size': '1vw'
                     }
                     ),
            html.H3(children='Credits', className="card-title"),
            html.Pre(children=credits_paragraph,
                     className="card-text",
                     style={
                         'white-space': 'pre-wrap',  # Allows text to wrap instead of extending in one line
                         'overflow': 'hidden',  # Prevents the scrollbar from appearing
                         'font-size': '1vw'
                     }
                     ),
            html.A('GitHub', className="sleek-link",
                   href='https://github.com/tledbet94'),
            html.P(''),
            html.A('LinkedIn', className="sleek-link",
                   href='https://www.linkedin.com/in/thomas-ledbetter-cfa%C2%AE-a4bb47120/'),
        ], className='home-card'
    ), className='home-card',
)

user = html.Div([
    user_card
])
