from dash import dcc
import dash_bootstrap_components as dbc

ai_user_input = dcc.Textarea(id='ai-input', placeholder='Provide input for ChatGPT 4o', className='edit-input',
                             style={'height': '50vh', 'width': '100%'})

ai_update_button = dbc.Button(
    id='ai-update-button',
    children="BUILD NEW",
    className="fields-update-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

ai_expand_button = dbc.Button(
    id='ai-expand-button',
    children="EXPAND",
    className="fields-update-button",
    style={'outline': 'none', 'margin_left': '15px'},
)

ai = dbc.Container(
    [
        dcc.Store('ai-elements'),
        dbc.Row(ai_user_input),
        dbc.Row([dbc.Col(ai_update_button), dbc.Col(ai_expand_button)], justify='center', style={'marginTop': '2vh'})
    ]
)
