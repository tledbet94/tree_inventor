import dash_cytoscape as cyto
import json
import random

cytoscape_background_color = '#352b42'
node_background_color = '#4b80ca'
node_border_color = '#68c2d3'
# edge_line_color = '#c28d75'
target_arrow_color = '#be955c'

cyto.load_extra_layouts()

stylesheet = [
    # Style all nodes
    {
        'selector': 'node',
        'style': {
            'height': '60px',
            'width': '60px',
            'background-color': node_background_color,
            'border-width': '4vh',
            'border-color': node_border_color,
            'border-style': 'solid',
            'label': 'data(label)',
            'text-valign': 'center',
            'text-halign': 'center',
            'color': '#f2f0e5',
            'font-size': '14px',
            'shape': 'circle',
            'border-opacity': 0.75,
            'background-opacity': 1,
            'overlay-opacity': 0
        }
    },
    {
        'selector': 'node:selected',
        'style': {
            'background-color': '#b45252',
            'border-color': '#d3a068',
            'overlay-opacity': 0  # Removes the default gray overlay box when selected
        }
    },
    {
        'selector': 'edge',
        'style': {
            # 'line-color': '#d3a068',  # Use the line color you defined
            'line-fill': 'linear-gradient',
            'line-gradient-stop-colors': '#43436a #4b80ca',
            'line-gradient-stop-positions': '0% 100%',
            'width': '5px',  # Set the edge thickness
            'line-style': 'solid',  # Optional: 'solid', 'dashed', 'dotted', etc.
            'curve-style': 'bezier',  # Optional: 'bezier', 'straight', etc.
            # Optional Arrowhead Styling
            'target-arrow-shape': 'circle',
            'target-arrow-color': '#a2dcc7',
            'arrow-scale': .6,  # Adjust arrow size as needed,
            'z-index': 2,
            'opacity': 0.9,
            'overlay-opacity': 0

        }
    },
    {
        'selector': 'edge:selected',
        'style': {
            'line-fill': 'linear-gradient',
            'line-gradient-stop-colors': '#b45252 #d3a068',
            'line-gradient-stop-positions': '0% 100%',
            'target-arrow-color': '#ede19e',
            'overlay-opacity': 0
        }
    },
    {
        'selector': '[traversed = "True"]',
        'style': {
            'background-color': '#8e478c',
            'line-gradient-stop-colors': '#564064 #cd6093',
            'border-color': '#cd6093',
            'target-arrow-color': '#ffaeb6',
            'overlay-opacity': 0
        }
    },
    {
        'selector': '[common = "True"]',
        'style': {
            'background-color': '#cd6093',
            'line-gradient-stop-colors': '#cd6093 #ffaeb6',
            'border-color': '#ffaeb6',
            'target-arrow-color': '#ffaeb6',
            'overlay-opacity': 0
        }
    },
    {
        'selector': '[invalid_weight = "True"]',
        'style': {
            'background-color': '#d3a068',
            'line-gradient-stop-colors': '#ede19e #d3a068',
            'border-color': '#ede19e',
            'target-arrow-color': '#e5ceb4',
            'overlay-opacity': 0
        }
    },
]


def random_number_as_string():
    numbers = {
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight"
    }
    random_num = random.randint(2, 8)
    return numbers[random_num]


r = random_number_as_string()

path = 'cytoscape/templates/' + r + '.json'

with open(path, "r") as json_file:
    loaded_elements = json.load(json_file)
    elements = loaded_elements['elements']
    file_info = {
        'name': loaded_elements['Name'],
        'description': loaded_elements['Description'],
        'author': loaded_elements['Author'],
        'theme_data': {
            'color': loaded_elements['theme_data']['color'],
            'shape': loaded_elements['theme_data']['shape'],
            'outline': loaded_elements['theme_data']['outline'],
            'pointer': loaded_elements['theme_data']['pointer'],
            'background': loaded_elements['theme_data']['background'],
        }

    }

cyto_component = cyto.Cytoscape(
    id='cytoscape',
    layout={'name': 'dagre', 'spacingFactor': 1, 'animate': True, 'animationDuration': 1000},
    style={
           'width': '100%',
           'backgroundColor': cytoscape_background_color,
           'border': '15px solid #868188',
           'borderRadius': '30px',
           'box-shadow': 'inset 0px 0px 10px 10px #646365'},
    elements=elements,
    stylesheet=stylesheet
)

# Fit the graph to the viewport when first loading
cyto_component.fit = {
    'padding': 50,  # Optional padding
    'fit': True  # Fit graph to the available space
}

# Ensure both `cyto_component` and `file_info` are available for import
__all__ = ['cyto_component', 'file_info']
