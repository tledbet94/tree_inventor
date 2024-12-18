from dash import callback, Input, Output, State
import json


@callback(
    Output('template-store', 'data'),
    [
        Input('template_one_button', 'active'),
        Input('template_two_button', 'active'),
        Input('template_three_button', 'active'),
        Input('template_four_button', 'active'),
        Input('template_five_button', 'active'),
        Input('template_six_button', 'active'),
        Input('template_seven_button', 'active'),
        Input('template_eight_button', 'active')
    ],
    [
        State('cytoscape', 'elements')
    ]
    # Use current elements as fallback
)
def swap_trees(
        active_one, active_two, active_three, active_four,
        active_five, active_six, active_seven, active_eight,
        current_elements
):
    # Map active states to template numbers
    active_states = [
        active_one, active_two, active_three, active_four,
        active_five, active_six, active_seven, active_eight
    ]

    # Map tree numbers to file paths
    template_files = {
        1: "cytoscape/templates/one.json",
        2: "cytoscape/templates/two.json",
        3: "cytoscape/templates/three.json",
        4: "cytoscape/templates/four.json",
        5: "cytoscape/templates/five.json",
        6: "cytoscape/templates/six.json",
        7: "cytoscape/templates/seven.json",
        8: "cytoscape/templates/eight.json"
    }

    # Determine which template button is active
    current_tree = None
    for i, active in enumerate(active_states, start=1):
        if active:
            current_tree = i
            break

    # If no button is active, return current elements in file-info
    if current_tree is None:
        return current_elements

    # Load the corresponding template
    if current_tree in template_files:
        try:
            with open(template_files[current_tree], "r") as json_file:
                loaded_elements = json.load(json_file)
                elements = loaded_elements['elements']
                return elements

        except FileNotFoundError:
            # Handle missing file gracefully
            return current_elements
    else:
        # Fallback: return current elements if no valid template is found
        return current_elements
