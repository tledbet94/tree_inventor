from dash import ctx, Input, Output, State
from app_instance import app
import json


@app.callback(
    Output('template-store', 'data'),
    [
        Input('template_one_button', 'active'),
        Input('template_two_button', 'active'),
        Input('template_three_button', 'active'),
        Input('template_four_button', 'active'),
        Input('template_five_button', 'active'),
        Input('template_six_button', 'active'),
        Input('template_seven_button', 'active'),
        Input('template_eight_button', 'active'),
    ],
    State('cytoscape', 'elements')
)
def swap_trees(one_active, two_active, three_active, four_active,
               five_active, six_active, seven_active, eight_active, current_elements):

    if one_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif two_active:
        with open("cytoscape/templates/two.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif three_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif four_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif five_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif six_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif seven_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    elif eight_active:
        with open("cytoscape/templates/one.json", "r") as json_file:
            loaded_elements = json.load(json_file)
            return loaded_elements
    else:
        return current_elements

