import random

def traverse_tree(elements, traversal_state):
    current_node_id = traversal_state['current_node_id']
    current_node = next(
        (e for e in elements if e['data']['id'] == current_node_id and 'source' not in e['data']), None)

    current_node_data = None

    if not current_node:
        # Node not found, end traversal
        traversal_state['finished'] = True
        return elements, traversal_state, current_node_data

    # Get node weight
    node_weight = current_node['data'].get('weight', 0)

    # Get outgoing edges from the current node
    outgoing_edges = [e for e in elements if e['data'].get('source') == current_node_id]

    # Build options for traversal
    options = []
    total_weight = node_weight
    options.append({'type': 'node', 'id': current_node_id, 'weight': node_weight})

    for edge in outgoing_edges:
        edge_weight = edge['data'].get('weight', 0)
        total_weight += edge_weight
        options.append({'type': 'edge', 'edge': edge, 'target': edge['data']['target'], 'weight': edge_weight})

    # If total_weight is zero, can't proceed
    if total_weight == 0:
        # No valid options, end traversal
        traversal_state['finished'] = True
        return elements, traversal_state, current_node_data

    # Select an option based on weights
    rand_val = random.uniform(0, total_weight)
    cumulative_weight = 0
    selected_option = None
    for option in options:
        cumulative_weight += option['weight']
        if rand_val <= cumulative_weight:
            selected_option = option
            break

    if selected_option['type'] == 'node':
        # Stop traversal at current node
        traversal_state['finished'] = True
        # Highlight the node
        for element in elements:
            if element['data']['id'] == selected_option['id'] and 'source' not in element['data']:
                element['selected'] = True
                current_node_data = element['data']
        return elements, traversal_state, current_node_data
    else:
        # Proceed to next node via edge
        next_node_id = selected_option['target']
        traversal_state['current_node_id'] = next_node_id
        traversal_state['path'].append(next_node_id)

        # Highlight the edge and the next node
        for element in elements:
            if element['data']['id'] == selected_option['edge']['data']['id']:
                element['selected'] = True
            elif element['data']['id'] == next_node_id and 'source' not in element['data']:
                element['selected'] = True
                current_node_data = element['data']

        return elements, traversal_state, current_node_data
