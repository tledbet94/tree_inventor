from dash import callback, Input, Output, State


@callback(
    [
        Output('card-title', 'children'),
        Output('card-author', 'children'),
        Output('card-description', 'children'),
    ],
    Input('file-info', 'data')
)
def update_card(file_info):
    print('updating card')
    print(file_info)
    return file_info['Name'], file_info['Author'], file_info['Description']
