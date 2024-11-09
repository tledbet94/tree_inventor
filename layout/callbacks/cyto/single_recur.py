import random
import copy

def single_traversal(elements, current_node_id='root', path=None):
    if path is None:
        path = [current_node_id]

    # Get the current node's data
    current_node = next((elem for elem in elements if elem['data'].get('id') == current_node_id and 'source' not in elem['data']), None)

    if not current_node:
        # If the current node is not found, terminate the traversal
        return path

    # Find all edges starting from the current node
    edges = [elem for elem in elements if elem['data'].get('source') == current_node_id]

    if not edges:
        # If there are no outgoing edges, it's a terminal node
        return path

    # Include the current node's weight and edges' weights for probability calculation
    total_weight = current_node['data'].get('weight', 0) + sum(edge['data']['weight'] for edge in edges)

    # Create a weighted choice list
    weighted_choices = [(current_node_id, current_node['data'].get('weight', 0))]  # Include the current node itself
    weighted_choices.extend((edge['data']['target'], edge['data']['weight']) for edge in edges)

    # Choose the next node based on the weighted probabilities
    next_node_id = random.choices(
        [choice[0] for choice in weighted_choices],
        weights=[choice[1] for choice in weighted_choices],
        k=1
    )[0]

    path.append(next_node_id)

    # Mark the selected edge if an edge was chosen (not the current node)
    if next_node_id != current_node_id:
        for edge in edges:
            if edge['data']['target'] == next_node_id:
                edge['traversed'] = True

    # If the chosen node is the current node, it is terminal
    if next_node_id == current_node_id:
        return path

    # Recursively traverse the chosen node
    return single_traversal(elements, current_node_id=next_node_id, path=path)
