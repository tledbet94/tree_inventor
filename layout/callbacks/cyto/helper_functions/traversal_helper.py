from collections import Counter
import random


def build_graph(elements):
    graph = {}
    node_weights = {}
    for element in elements:
        data = element['data']
        if 'source' in data and 'target' in data:
            # It's an edge
            source = data['source']
            target = data['target']
            weight = data.get('weight', 0)
            if source not in graph:
                graph[source] = []
            graph[source].append((target, weight))
        elif 'id' in data and 'source' not in data and 'target' not in data:
            # It's a node
            node_id = data['id']
            weight = data.get('weight', 0)
            node_weights[node_id] = weight
            if node_id not in graph:
                graph[node_id] = []

    return graph, node_weights


def single_traversal_with_steps(graph, node_weights, current_node_id='root', path=None):
    if path is None:
        path = [current_node_id]

    # Get the current node's weight
    current_node_weight = node_weights.get(current_node_id, 0)

    # Get the edges from the current node
    edges = graph.get(current_node_id, [])

    if not edges:
        # If there are no outgoing edges, it's a terminal node
        return path

    # Include the current node's weight and edges' weights for probability calculation
    weighted_choices = [(current_node_id, current_node_weight)]  # Include the current node itself
    weighted_choices.extend(edges)

    # Choose the next node based on the weighted probabilities
    next_node_id = random.choices(
        [choice[0] for choice in weighted_choices],
        weights=[choice[1] for choice in weighted_choices],
        k=1
    )[0]

    path.append(next_node_id)

    # If the chosen node is the current node, it is terminal
    if next_node_id == current_node_id:
        return path

    # Recursively traverse the chosen node
    return single_traversal_with_steps(graph, node_weights, current_node_id=next_node_id, path=path)


def multiple_traversals_batch(graph, node_weights, batch_size, state=None):
    if state is None:
        state = {
            'terminal_node_counts': Counter(),
            'path_counts': Counter(),
            'most_common_node_id': None,
            'most_common_path': [],
            'all_visited_nodes': set(),
            'all_visited_edges': set(),
        }
    else:
        # Convert lists back to sets and Counters
        state['all_visited_nodes'] = set(state.get('all_visited_nodes', []))
        state['all_visited_edges'] = set(tuple(edge) for edge in state.get('all_visited_edges', []))
        state['path_counts'] = Counter(state.get('path_counts', {}))
        state['terminal_node_counts'] = Counter(state.get('terminal_node_counts', {}))

    for _ in range(batch_size):
        path = single_traversal_with_steps(graph, node_weights)
        terminal_node = path[-1]
        state['terminal_node_counts'][terminal_node] += 1
        path_tuple = tuple(path)
        state['path_counts'][path_tuple] += 1

        # Collect visited nodes and edges
        state['all_visited_nodes'].update(path)
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            state['all_visited_edges'].add((source, target))

    # Update the most common node
    most_common_node = state['terminal_node_counts'].most_common(1)
    if most_common_node:
        state['most_common_node_id'] = most_common_node[0][0]
    else:
        state['most_common_node_id'] = None

    # Find the most common path
    most_common_path = state['path_counts'].most_common(1)
    if most_common_path:
        state['most_common_path'] = most_common_path[0][0]
    else:
        state['most_common_path'] = []

    # Convert sets back to lists for JSON serialization
    state['all_visited_nodes'] = list(state['all_visited_nodes'])
    state['all_visited_edges'] = [list(edge) for edge in state['all_visited_edges']]
    state['path_counts'] = {str(k): v for k, v in state['path_counts'].items()}
    state['terminal_node_counts'] = dict(state['terminal_node_counts'])

    return state
