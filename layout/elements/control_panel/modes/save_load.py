from dash import dcc, html
import dash_bootstrap_components as dbc

save_load_title = html.H1('Save & Load', className='edit-header-text')

local_save_text = html.Div(html.P(children="Download Tree", className="theme-font"),
                           style={'textAlign': 'center'})

local_save_input = dbc.Input(id='local-save-input', placeholder='Enter a file name', className='edit-input')

local_save_button = dbc.Button(children=html.I(className="fa-solid fa-download icon-style-bottom-row"),
                               id='local-save-button', className='themes-apply-button')

local_save_dummy = dcc.Store(id='local_save_dummy')

local_download = dcc.Download(id='local-download')

save_load = html.Div(
    [
        local_save_dummy,
        local_download,
        save_load_title,
        html.Div(style={'height': '6vh'}),
        local_save_text,
        dbc.Row([dbc.Col(local_save_input, align='center', width=8), dbc.Col(local_save_button, width=4)]),
    ]
)
