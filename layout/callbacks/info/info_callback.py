# info_callback.py
from dash import Input, Output, callback_context
from app import app

@app.callback(
    [
        Output('node-name', 'children'),
        Output('node-weight', 'children'),
        Output('node-level', 'children'),
        Output('node-custom1', 'children'),
        Output('node-custom2', 'children'),
        Output('node-custom3', 'children'),
        ],
    [
        Input('cytoscape', 'tapNodeData'),
        Input('cytoscape', 'tapEdgeData'),
        Input('cytoscape', 'selectedNodeData'),
        Input('cytoscape', 'selectedEdgeData'),
        Input('name-store', 'data')
    ]
)
def update_node_name(tap_node_data, tap_edge_data, selected_node_data, selected_edge_data, name_store):
    ctx = callback_context
    triggered_prop = ctx.triggered[0]['prop_id'] if ctx.triggered else ''

    # Initialize variables
    node_data = None
    edge_data = None

    # Prioritize tapNodeData and tapEdgeData
    if 'tapNodeData' in triggered_prop and tap_node_data:
        node_data = tap_node_data
    elif 'tapEdgeData' in triggered_prop and tap_edge_data:
        edge_data = tap_edge_data
    # Next, check selectedNodeData and selectedEdgeData
    elif selected_node_data:
        node_data = selected_node_data[-1]  # Use the last selected node
    elif selected_edge_data:
        edge_data = selected_edge_data[-1]

    if node_data:
        # Process node data
        name = str(node_data.get('label', 'N/A'))
        weight = str(node_data.get('weight', 'N/A')) + '%'
        level = 'L' + str(node_data.get('level', 'N/A'))
        custom1 = str(node_data.get('Productive?', 'N/A'))
        custom2 = str(node_data.get('Mood Impact', 'N/A'))
        custom3 = str(node_data.get('Fun Level', 'N/A'))

        # Use name_store if available
        if name_store:
            name = name_store

        return name, weight, level, custom1, custom2, custom3

    elif edge_data:
        # Process edge data
        name = 'Edge'
        weight = str(edge_data.get('weight', 'N/A')) + '%'
        level = '-'
        custom1 = '-'
        custom2 = '-'
        custom3 = '-'

        return name, weight, level, custom1, custom2, custom3

    # If name_store is provided, use it to update the name
    if name_store:
        return name_store, '-', '-', '-', '-', '-'

    # No data available
    return '-', '-', '-', '-', '-', '-'
