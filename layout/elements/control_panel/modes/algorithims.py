from dash import dcc, html
import dash_bootstrap_components as dbc

algo_title = html.H1('ALGORITHIMS')

single_traversal_button = dbc.Button(
    id='single-traversal-button',
    children="SINGLE TRAVERSAL",
    className="algo-button",
)

multiple_traversal_button = dbc.Button(
    id='multiple-traversal-button',
    children="MULTIPLE TRAVERSAL",
    className="algo-button",
)

algo = dbc.Container([
    dbc.Row(
        dbc.Col(
            algo_title
        ),
        justify="center",
    ),
    dbc.Row([
        html.Div(style={"height": "8vh"}),
        dbc.Col(width=1),
        dbc.Col(single_traversal_button, align='center'),
        dbc.Col(width=1)
    ], justify='center'),
    html.Div(style={"height": "8vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(multiple_traversal_button, align='center'),
        dbc.Col(width=1)
    ], justify='center')
],
    fluid=True,
)
