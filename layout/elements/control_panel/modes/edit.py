from dash import dcc, html
import dash_bootstrap_components as dbc

# Add hover instructions at the top
# Function to add a child node, remove node(s), or rename node

# Add node - requires input
# Rename node - requires input
# Remove node - does not require input
# So put in that order?

# Prompt for input after pressing button, have enter button appear

rename_info = html.Div(
    [
        html.P(
            html.I(
                className="fa-solid fa-question icon-style-question-mark",
                id="rename-tooltip-target",  # Add an ID for the tooltip target
                style={"cursor": "pointer"},  # Optional: pointer cursor for better UX
            ),
        ),
        dbc.Tooltip(
            "Change the label of the selected node through user input",
            target="rename-tooltip-target",  # Match this to the ID above
        ),
    ]
)

add_info = html.Div(
    [
        html.P(
            html.I(
                className="fa-solid fa-question icon-style-question-mark",
                id="add-tooltip-target",  # Unique ID for the tooltip target
                style={"cursor": "pointer"},
            ),
        ),
        dbc.Tooltip(
            "Add a child to the selected node with the input label; \nweight and other properties will default",
            target="add-tooltip-target",  # Match this to the ID above
        ),
    ]
)

remove_info = html.Div(
    [
        html.P(
            html.I(
                className="fa-solid fa-question icon-style-question-mark",
                id="remove-tooltip-target",  # Unique ID for the tooltip target
                style={"cursor": "pointer"},
            ),
        ),
        dbc.Tooltip(
            "Remove the selected node - if the selected node is a branch, all its children will be deleted.\n"
            "The root cannot be deleted.",
            target="remove-tooltip-target",  # Match this to the ID above
        ),
    ]
)

rename_node_button = dbc.Button(
    id='rename-button',
    children=html.I(className="fa-solid fa-pencil icon-style-edit"),
    className="edit-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

add_node_button = dbc.Button(
    id='add-button',
    children=html.I(className="fa-solid fa-plus icon-style-edit"),
    className="edit-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

remove_node_button = dbc.Button(
    id='remove-button',
    children=html.I(className="fa-solid fa-minus icon-style-edit"),
    className="edit-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

edit_input = dbc.Input(placeholder='', size='lg', valid=False, className='edit-input')
edit_input_button = dbc.Button(children='ENTER', className='edit-input-button')
edit_input_feedback = html.Div(
    html.P('Placeholder', id='edit-input-feedback', style=({'color': '#f2f0e5', 'font-size': '18px'})),
    style={'backgroundColor': '#8ab060', 'height': '10vh', "border": "5px solid #4e584a"}
)

edit = html.Div([
    html.H1('MODIFY TREE', style={'color': '#646365', 'font-weight': 'bold', 'text-align': 'center',
                                  'text-shadow': '-2px -2px 1px #45444f', 'font-size': '4rem'}),
    html.Div(style={"height": "5vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(rename_node_button, width=7),
        dbc.Col(rename_info, align='end', width=3)
    ]),
    html.Div(style={"height": "10vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(add_node_button, width=7),
        dbc.Col(add_info, align='end', width=3)
    ]),
    html.Div(style={"height": "10vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(remove_node_button, width=7),
        dbc.Col(remove_info, align='end', width=3),
    ]),
    html.Div(style={"height": "5vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(edit_input_feedback),
        dbc.Col(width=3)
    ]),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(edit_input, width=8),
        dbc.Col(edit_input_button, width=3),
    ])
])
