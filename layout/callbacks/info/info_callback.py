from dash import Input, Output
from app_instance import app


@app.callback(
    Output('node-name', 'children'),
    Output('node-weight', 'children'),
    Output('node-custom1', 'children'),
    Output('node-custom2', 'children'),
    Output('node-custom3', 'children'),
    [Input('cytoscape', 'tapNodeData')]
)
def update_node_name(node_data):
    if node_data is None:
        return '', '', '', '', ''
    else:
        print(node_data)
    name = str(node_data['label'])
    weight = str(node_data['weight'])
    custom1 = str(node_data['Productive?'])
    custom2 = str(node_data['Mood Impact'])
    custom3 = str(node_data['Fun Level'])
    return name, weight, custom1, custom2, custom3
