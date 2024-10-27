from dash import Input, Output
from app_instance import app


@app.callback(
    Output('node-name', 'children'),
    [Input('cytoscape', 'tapNodeData')]
)
def update_node_name(node_data):
    print(node_data)
    if node_data is None:
        return ''
    return str(node_data['label'])
