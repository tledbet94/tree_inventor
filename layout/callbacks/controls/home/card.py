from dash import Input, Output, State
from app_instance import app




@app.callback(
    [
        Output('card-title', 'children'),
        Output('card-author', 'children'),
        Output('card-description', 'children'),
    ],
    Input('file-info', 'data')
)
def update_card(file_info):
    return file_info['Name'], file_info['Author'], file_info['Description']
