from dash import dcc, html
import dash_bootstrap_components as dbc

# Tooltips section
# _info variables represent the tool tips / question marks in app

rename_info = html.Div(
    [
        html.P(
            html.I(
                className='fa-solid fa-question icon-style-question-mark',
                id='rename-tooltip-target',  # Add an ID for the tooltip target
                style={'cursor': 'pointer'},  # Optional: pointer cursor for better UX
            ),
        ),
        dbc.Tooltip(
            'Change the label of the selected node.',
            target='rename-tooltip-target',  # Match this to the ID above
            style={'font-size': '1vw'}
        ),
    ]
)

add_info = html.Div(
    [
        html.P(
            html.I(
                className='fa-solid fa-question icon-style-question-mark',
                id='add-tooltip-target',  # Unique ID for the tooltip target
                style={'cursor': 'pointer'},
            ),
        ),
        dbc.Tooltip(
            'Add a child to the selected node; \nprovide a label for the new node',
            target='add-tooltip-target',  # Match this to the ID above
            style={'font-size': '1vw'}
        ),
    ]
)

remove_info = html.Div(
    [
        html.P(
            html.I(
                className='fa-solid fa-question icon-style-question-mark',
                id='remove-tooltip-target',  # Unique ID for the tooltip target
                style={'cursor': 'pointer'},
            ),
        ),
        dbc.Tooltip(
            'Remove a node and its children - there is no undo button!',
            target='remove-tooltip-target',  # Match this to the ID above
            style={'font-size': '1vw'}
        ),
    ]
)

# Buttons section

rename_node_button = dbc.Button(
    id='rename-button',
    children=html.I(className='fa-solid fa-pencil icon-style-edit'),
    className='edit-button',
    style={'outline': 'none'},
)

add_node_button = dbc.Button(
    id='add-button',
    children=html.I(className='fa-solid fa-plus icon-style-edit'),
    className='edit-button',
    style={'outline': 'none'},
)

remove_node_button = dbc.Button(
    id='remove-button',
    children=html.I(className='fa-solid fa-minus icon-style-edit'),
    className='edit-button',
    style={'outline': 'none'},
)

# Edit input, enter button, and feedback screen
# Invisible by default
# Only appear when conditions are met (e.g. add node is pressed, node selected, input is not blank)
edit_input = (
    dbc.Input(id='edit-input', placeholder='', size='lg', valid=False, className='edit-input'))

edit_input_button = (
    dbc.Button(id='edit-input-button', children='ENTER', className='hidden-opacity'))

edit_input_feedback = (
    html.Div(
        html.P('Placeholder', id='edit-input-feedback', className='edit-input-font'),
        className='input-feedback-div'
    ))

# Layout
# dbc width and vh are key to spacing
edit = html.Div([
    dcc.Store(id='edit-enter-click-store', data=0),
    dcc.Store(id='enter-pressed-bool', data=False),
    dcc.Store(id='selected-edit', data=''),
    dbc.Row([
        dbc.Col(rename_node_button, width=4),
        dbc.Col(rename_info, align='end', width=2),
        dbc.Col(add_node_button, width=4),
        dbc.Col(add_info, align='end', width=2)
    ]),
    html.Div(style={'height': '3vh'}),
    dbc.Row([
        dbc.Col(remove_node_button, width=4),
        dbc.Col(remove_info, align='end', width=2),
        dbc.Col(width=6)
    ]),
    html.Div(style={'height': '4vh'}),
    dbc.Row([
        dbc.Col(edit_input_feedback),
    ], id='edit-input-feedback-row', className='hidden-opacity'),
    html.Div(style={'height': '2vh'}),
    dbc.Row([
        dbc.Col(edit_input, width=8),
        dbc.Col(edit_input_button, width=3, align='center'),
        dbc.Col(width=1),
    ], id='edit-input-row', className='hidden-opacity')
])
