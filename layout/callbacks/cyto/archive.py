def single_traversal_with_steps(elements, current_node_id='root', steps=None):
    elements = copy.deepcopy(elements) if elements else []
    if steps is None:
        steps = [current_node_id]
        random.seed(time.time() + random.random())  # Better randomness

    # Find children of the current node
    children = [elem['data']['target'] for elem in elements if elem['data'].get('source') == current_node_id]

    if not children:
        # Reached a terminal node
        return steps

    # Choose the next node (randomly for this example)
    next_node_id = random.choice(children)
    steps.append(next_node_id)

    # Recursively traverse the next node
    return single_traversal_with_steps(elements, current_node_id=next_node_id, steps=steps)

def multiple_traversals(elements, num_traversals):
    elements = copy.deepcopy(elements)
    terminal_nodes = []
    paths = []

    for i in range(num_traversals):
        path = single_traversal_with_steps(elements)
        paths.append(path)
        terminal_nodes.append(path[-1])  # The last node in the path is the terminal node

        # Print statements for debugging
        # print(f"Traversal {i + 1}/{num_traversals} completed.")
        # print(f"Path taken: {path}")
        # print(f"Terminal node reached: {path[-1]}")

    # Count the occurrences of each terminal node
    terminal_node_counts = Counter(terminal_nodes)
    most_common_node_id, _ = terminal_node_counts.most_common(1)[0]

    return {
        'paths': paths,
        'terminal_node_counts': terminal_node_counts,
        'most_common_node_id': most_common_node_id
    }