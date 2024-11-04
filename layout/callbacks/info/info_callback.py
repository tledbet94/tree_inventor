from dash import Input, Output, callback_context
from app import app

@app.callback(
    [Output('node-name', 'children'),
     Output('node-weight', 'children'),
     Output('node-level', 'children'),
     Output('node-custom1', 'children'),
     Output('node-custom2', 'children'),
     Output('node-custom3', 'children')],
    [Input('cytoscape', 'tapNodeData'),
     Input('cytoscape', 'tapEdgeData'),
     Input('name-store', 'data')]
)
def update_node_name(node_data, edge_data, name_store):
    ctx = callback_context

    if not ctx.triggered:
        return '-', '-', '-', '-', '-', '-'

    triggered_prop = ctx.triggered[0]['prop_id'].split('.')[1]

    if triggered_prop == 'tapNodeData':
        # Process node data
        name = str(node_data.get('label', 'N/A'))
        weight = str(node_data.get('weight', 'N/A')) + '%'
        level = 'L' + str(node_data.get('level', 'N/A'))
        custom1 = str(node_data.get('Productive?', 'N/A'))
        custom2 = str(node_data.get('Mood Impact', 'N/A'))
        custom3 = str(node_data.get('Fun Level', 'N/A'))

        if name == name_store or name_store == '':
            return name, weight, level, custom1, custom2, custom3
        else:
            return name_store, weight, level, custom1, custom2, custom3

    elif triggered_prop == 'tapEdgeData':
        # Process edge data
        name = 'Edge'
        weight = str(edge_data.get('weight', 'N/A')) + '%'
        level = '-'
        custom1 = '-'
        custom2 = '-'
        custom3 = '-'

        return name, weight, level, custom1, custom2, custom3

    else:
        return '-', '-', '-', '-', '-', '-'
