from collections import Counter
from .single_recur import single_traversal

def multiple_traversals(elements, num_traversals):
    terminal_nodes = []
    paths = []
    all_visited_nodes = set()
    all_visited_edges = set()
    path_counts = Counter()

    for _ in range(num_traversals):
        path = single_traversal(elements)
        paths.append(path)
        terminal_nodes.append(path[-1])  # The last node in the path is the terminal node
        all_visited_nodes.update(path)  # Collect all visited nodes
        path_counts[tuple(path)] += 1    # Count the occurrence of each path

        # Collect visited edges
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            all_visited_edges.add((source, target))

    # Count the occurrences of each terminal node
    terminal_node_counts = Counter(terminal_nodes)
    most_common_node_id, _ = terminal_node_counts.most_common(1)[0]

    # Find the most common path
    most_common_path, _ = path_counts.most_common(1)[0]
    most_common_nodes = set(most_common_path)
    most_common_edges = set(zip(most_common_path[:-1], most_common_path[1:]))

    # Reset attributes and update elements to mark traversed and common nodes and edges
    for element in elements:
        data = element['data']
        data['traversed'] = False  # Reset traversed attribute
        data['common'] = False     # Reset common attribute

        # Mark traversed nodes and edges
        if data['id'] in all_visited_nodes:
            data['traversed'] = True

        # Mark common nodes and edges
        if data['id'] in most_common_nodes:
            data['common'] = True

        if 'source' in data:
            edge_tuple = (data['source'], data['target'])
            if edge_tuple in all_visited_edges:
                data['traversed'] = True

            if edge_tuple in most_common_edges:
                data['common'] = True

    return {
        'paths': paths,
        'terminal_node_counts': terminal_node_counts,
        'most_common_node_id': most_common_node_id
    }
