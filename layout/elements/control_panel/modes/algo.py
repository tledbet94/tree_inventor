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

# Input components only appear when they are needed
edit_input = (
    dbc.Input(id='edit-input', placeholder='', size='lg', valid=False, className='edit-input'))

edit_input_button = (
    dbc.Button(id='edit-input-button', children='ENTER', className='hidden-opacity'))

edit_input_feedback = (
    html.Div(
        html.P('Placeholder', id='edit-input-feedback', className='edit-input-font'),
        className='input-feedback-div'
    ))

edit = html.Div([
    dcc.Store(id='edit-enter-click-store', data=0),
    dcc.Store(id='enter-pressed-bool', data=False),
    dcc.Store(id='selected-edit', data=''),
    html.H1('MODIFY TREE', className='edit-header-text'),
    html.Div(style={"height": "5vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(rename_node_button, width=5),
        dbc.Col(rename_info, align='end', width=5)
    ]),
    html.Div(style={"height": "5vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(add_node_button, width=5),
        dbc.Col(add_info, align='end', width=5)
    ]),
    html.Div(style={"height": "5vh"}),
    dbc.Row([
        dbc.Col(width=2),
        dbc.Col(remove_node_button, width=5),
        dbc.Col(remove_info, align='end', width=5),
    ]),
    html.Div(style={"height": "8vh"}),
    dbc.Row([
        dbc.Col(edit_input_feedback),
    ], id='edit-input-feedback-row', className='hidden-opacity'),
    html.Div(style={"height": "3vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(edit_input, width=8),
        dbc.Col(edit_input_button, width=3),
    ], id='edit-input-row', className='hidden-opacity')
])
