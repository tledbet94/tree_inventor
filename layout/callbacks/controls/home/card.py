from dash import Input, Output, State
from app_instance import app


@app.callback(
    [
        Output('card-title', 'children'),
        Output('card-author', 'children'),
        Output('card-description', 'children'),
    ],
    Input('home-button', 'active'),
    State('file-info', 'data')
)
def update_card(home_active, file_info):
    return file_info['name'], file_info['author'], file_info['description']
