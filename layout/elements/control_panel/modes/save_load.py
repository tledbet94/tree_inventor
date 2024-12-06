from dash import dcc, html
import dash_bootstrap_components as dbc

save_load_title = html.H1('Save & Load', className='edit-header-text')


# Download section
local_save_text = html.Div(html.P(children="Download Tree", className="save-load-text"),
                           style={'textAlign': 'center'})
# description
description_text = html.Div(html.P(children="Description: ", className="save-load-text"),
                      style={'textAlign': 'center'})

# author, title

local_save_input = dbc.Input(id='local-save-input', placeholder='Enter title', className='edit-input')

local_save_button = dbc.Button(children=html.I(className="fa-solid fa-download icon-style-bottom-row"),
                               id='local-save-button', className='save-load-button')

local_save_dummy = dcc.Store(id='local_save_dummy')

local_download = dcc.Download(id='local-download')

# load
local_load_text = html.Div(html.P(children="Upload Tree", className="save-load-text"),
                           style={'textAlign': 'center'})

upload_area = html.Div(dcc.Upload(
    id='upload-button',
    children=html.P('Drag & Drop || Click to Select File'),
    multiple=False,  # Set to True if you want to allow multiple files
    className='upload-area'
), style={'text-align': 'center'})

save_load = html.Div(
    [
        local_save_dummy,
        local_download,
        save_load_title,
        html.Div(style={'height': '4vh'}),
        local_save_text,
        dbc.Row([dbc.Col(local_save_input, align='center', width=8), dbc.Col(local_save_button, width=4)]),
        html.Div(style={'height': '4vh'}),
        local_load_text,
        dbc.Row(dbc.Col(upload_area))
    ]
)
