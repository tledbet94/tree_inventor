from dash import dcc, html
import dash_bootstrap_components as dbc

weights_title = html.H1('WEIGHTS', className='edit-header-text')

# Elements to type / enter/ validate
# Input components only appear when they are needed
weights_input_feedback = (
    html.Div(
        html.P('Select a Node and enter a weight.', id='weights-input-feedback', className='weights-input-font'),
        className='input-feedback-div-weights', style={'width': '95%'}
    ))

weights_input = (
    dbc.Input(id='weights-input', placeholder='', size='lg', valid=False, className='weights-input'))

weights_input_button = (
    dbc.Button(id='weights-input-button', children='ENTER', className='hidden-opacity'))

# buttons to select mode

manual_button = dbc.Button(
    id='manual-button',
    children=html.P("MANUAL"),
    className="auto-manual-button",
    style={'outline': 'none'},
)

auto_button = dbc.Button(
    id='auto-button',
    children=html.P("AUTOMATIC"),
    className="auto-manual-button",
    style={'outline': 'none'},
    disabled=False
)

# in manual mode, another set of input elements appears

manual_input_feedback = html.Div(
    html.P(
        'Weights in system must equal 100%',
        id='manual-input-feedback',
        className='weights-input-font'
    ),
    className='input-feedback-div-weights',
    style={'width': '95%', 'height': '20vh'}
)

system_weights_progress = dbc.Progress(
    value=0,
    id="system-weights-progress",
    animated=False,
    striped=False,
    style={
        'display': 'block',
        'margin-left': '15px'
    },
    class_name='algo-progress',
    max=100,
    min=0
)

# Layout - note use of vh and dbc width
weights = html.Div([
    dcc.Store(id='weights-enter-click-store', data=0),
    weights_title,
    html.Div(style={"height": "2vh"}),
    dbc.Row([
        dbc.Col(weights_input_feedback)
    ], id='weights-input-feedback-row', justify='center'),
    html.Div(style={"height": "3vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(weights_input, width=8),
        dbc.Col(weights_input_button, width=3)
    ], id='weights-input-row'),
    html.Div(style={"height": "5vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(auto_button, width=4),
        dbc.Col(width=1),
        dbc.Col(manual_button, width=4),
        dbc.Col(width=1)
    ], id='manual-auto-row', className='hidden-opacity'),
    html.Div(style={"height": "8vh"}),
    dbc.Row([
        dbc.Col(manual_input_feedback)
    ], id='manual-feedback-row', className='hidden-opacity', justify='center'),
    html.Div(style={"height": "3vh"}),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(system_weights_progress),
        dbc.Col(width=1),
    ], id='weights-progress-row', className='hidden-opacity', justify='center'),
    html.Div(style={"height": "3vh"})
])
