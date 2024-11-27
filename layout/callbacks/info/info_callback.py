from dash import Input, Output, State, callback_context
from app_instance import app
import json


@app.callback(
    [
        Output('node-name', 'children'),
        Output('node-weight', 'children'),
        Output('node-level', 'children'),
    ],
    [
        Input('cytoscape', 'tapNodeData'),
        Input('cytoscape', 'tapEdgeData'),
        Input('cytoscape', 'selectedNodeData'),
        Input('cytoscape', 'selectedEdgeData'),
        Input('cytoscape', 'elements'),
    ],
    [
        State('info-panel-data', 'data'),  # To store previous data
    ]
)
def update_node_info(tap_node_data, tap_edge_data, selected_node_data, selected_edge_data, elements,
                     info_panel_data):
    ctx = callback_context
    triggered_prop = ctx.triggered[0]['prop_id'] if ctx.triggered else ''

    # Initialize variables
    node_data = None
    edge_data = None

    # Determine if elements have changed
    elements_json = json.dumps(elements, sort_keys=True)
    previous_elements_json = info_panel_data.get('elements_json') if info_panel_data else None

    # Update info panel if elements have changed and an element is selected
    elements_changed = elements_json != previous_elements_json

    if 'tapNodeData' in triggered_prop and tap_node_data:
        node_data = tap_node_data
    elif 'tapEdgeData' in triggered_prop and tap_edge_data:
        edge_data = tap_edge_data
    elif elements_changed:
        # Elements have changed, find the selected node or edge
        if selected_node_data:
            node_data = selected_node_data[-1]  # Use the last selected node
        elif selected_edge_data:
            edge_data = selected_edge_data[-1]
    elif selected_node_data:
        node_data = selected_node_data[-1]
    elif selected_edge_data:
        edge_data = selected_edge_data[-1]

    if node_data:
        # Process node data
        name = str(node_data.get('label', 'N/A'))
        weight = str(node_data.get('weight', 'N/A')) + '%'
        level = 'L' + str(node_data.get('level', 'N/A'))

        return name, weight, level

    elif edge_data:
        # Process edge data
        name = 'Edge'
        weight = str(edge_data.get('weight', 'N/A')) + '%'
        level = '-'

        # Update stored elements
        info_panel_data = {'elements_json': elements_json}

        return name, weight, level

    # No data available
    info_panel_data = {'elements_json': elements_json}
    return '-', '-', '-',
