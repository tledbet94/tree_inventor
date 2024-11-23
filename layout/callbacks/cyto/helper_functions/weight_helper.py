import math


def get_system_info(elements):
    # Identify the selected element
    selected_element = None
    element_type = 'node'
    for element in elements:
        if element['data'].get('last_clicked') == 'True':
            selected_element = element
            if 'source' in element['data']:  # If 'source' exists, it's an edge
                element_type = 'edge'
            break  # Only one element should be last clicked

    if not selected_element:
        return None, None, [], 0, "No element selected."

    # Use a list to track system elements and avoid duplicates manually
    system_elements = [selected_element]

    if element_type == 'node':
        # If the selected element is a node, add all outgoing edges
        node_id = selected_element['data']['id']
        for element in elements:
            if 'source' in element['data'] and element['data']['source'] == node_id:
                if element not in system_elements:
                    system_elements.append(element)

    elif element_type == 'edge':
        # If the selected element is an edge, add the source node and all outgoing edges from that node
        source_node_id = selected_element['data']['source']

        # Add the source node
        for element in elements:
            if element['data']['id'] == source_node_id and element not in system_elements:
                system_elements.append(element)
                break

        # Add all outgoing edges from the source node (including the selected edge itself)
        for element in elements:
            if 'source' in element['data'] and element['data']['source'] == source_node_id:
                if element not in system_elements:
                    system_elements.append(element)

    # Calculate the system weight
    print(system_elements)
    system_weight = sum(element['data'].get('weight', 0) for element in system_elements)

    # Determine validity and set appropriate messages
    print(system_weight)
    if abs(system_weight - 100.0) > 0.01:
        # Mark elements as having an invalid weight if system weight is not 100%
        for element in system_elements:
            element['data']['invalid_weight'] = 'True'
        if system_weight > 100:
            message = f"Invalid | System weight above 100% ({system_weight:.2f}%)"
        else:
            message = f"Invalid | System weight below 100% ({system_weight:.2f}%)"
    else:
        # Mark elements as having a valid weight
        for element in system_elements:
            element['data']['invalid_weight'] = 'False'
        message = 'Valid | System weight equals 100%'

    return selected_element, element_type, system_elements, system_weight, message


def auto_balance_system(elements):
    selected_element, element_type, system_elements, system_weight, _ = get_system_info(elements)

    message = 'Automatic balance complete.'

    if not selected_element:
        return elements, "No element selected."

    # Extract the selected_element's weight (fixed)
    selected_weight = selected_element['data'].get('weight', 0)

    # Exclude the selected element from the list of system elements
    other_elements = [elem for elem in system_elements if elem != selected_element]
    num_other_elements = len(other_elements)

    if num_other_elements == 0:
        # Only the selected element in the system
        # Set its weight to 100%
        selected_element['data']['weight'] = round(100.0, 2)
        message = "Only one element in the system. Its weight has been set to 100%."
        return elements, message

    # Calculate the weight to distribute among other elements
    weight_to_distribute = 100.0 - selected_weight

    # Distribute the weight_to_distribute equally among other elements
    equal_weight = weight_to_distribute / num_other_elements

    # Update the weights of other elements
    for elem in other_elements:
        elem['data']['weight'] = equal_weight

    # Round weights to two decimal places
    selected_element['data']['weight'] = round(selected_element['data']['weight'], 2)
    for elem in other_elements:
        elem['data']['weight'] = round(elem['data']['weight'], 2)

    return elements, message


def proximity_to_100(x):
    print(x)
    if x <= 0:
        raise ValueError("x must be greater than 0 to calculate proximity in a meaningful way.")

    # Calculate absolute difference from 100
    difference = abs(100 - x)

    # Calculate the proximity percentage on a logarithmic scale
    proximity = 100 / (1 + math.log10(1 + difference))

    # Round to 2 decimal places for readability
    proximity = round(proximity, 2)

    # Ensure the proximity does not go below 1%
    proximity = max(1, proximity)

    return proximity
