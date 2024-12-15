from dash import dcc, html
import dash_bootstrap_components as dbc

save_load_title = html.H1('Save & Load', className='edit-header-text')

# Download section
local_save_text = html.Div(html.P(children="Download/Upload", className="save-load-text"),
                           style={'textAlign': 'center'})

# author, title

local_save_input = dbc.Input(id='local-save-input', placeholder='Enter title', className='edit-input')

author_input = dbc.Input(id='author-input', placeholder='Enter author', className='edit-input')

description_input = dcc.Textarea(id='description-input', placeholder='Enter description', className='edit-input',
                                 style={'height': '15vh', 'width': '100%'})

local_save_button = dbc.Button(children=html.I(className="fa-solid fa-download icon-style-bottom-row"),
                               id='local-save-button', className='save-load-button')

local_save_dummy = dcc.Store(id='local_save_dummy')

local_download = dcc.Download(id='local-download')

# load
local_load_text = html.Div(html.P(children="Upload Tree", className="save-load-text"),
                           style={'textAlign': 'center'})

upload_area = html.Div(dcc.Upload(
    id='upload-area',
    children=html.P(children='Drag & Drop || Click to Select File', style={'marginTop': '1vh'}),
    multiple=False,  # Set to True if you want to allow multiple files
    className='upload-area'
), style={'text-align': 'center'})

save_load = html.Div(
    [
        local_save_dummy,
        local_download,
        dcc.Store('upload-store'),
        dcc.Store('upload-active', data=True),
        local_save_text,
        dbc.Row([dbc.Col(local_save_input, align='center', width=8), dbc.Col(local_save_button, width=4)]),
        html.Div(style={'height': '2vh'}),
        dbc.Row(dbc.Col(author_input)),
        html.Div(style={'height': '2vh'}),
        dbc.Row(dbc.Col(description_input)),
        html.Div(style={'height': '3vh'}),
        dbc.Row(dbc.Col(upload_area))
    ]
)