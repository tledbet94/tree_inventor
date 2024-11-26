from dash import Input, Output, State, exceptions, dcc
from app_instance import app
import json


@app.callback(
    Output('local-download', 'data'),
    Input('local-save-button', 'n_clicks'),
    State('local-save-input', 'value'),
    State('cytoscape', 'elements'),
    prevent_initial_call=True
)
def local_save(save_clicks, file_name, current_tree):
    if not save_clicks:
        raise exceptions.PreventUpdate

    if not file_name:
        file_name = 'DAG_tree'
    file_name += '.json'

    content = json.dumps(current_tree)

    return dcc.send_string(content, filename=file_name)
