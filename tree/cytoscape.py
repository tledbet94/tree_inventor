import dash_cytoscape as cyto

# Internal imports
from .elements import default_elements

cytoscape_background_color = '#666092'
node_background_color = '#be955c'
node_border_color = '#8d6268'
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
            'border-width': '8px',
            'border-color': node_border_color,
            'border-style': 'solid',
            'label': 'data(label)',
            'text-valign': 'center',
            'text-halign': 'center',
            'color': '#c5ccb8',
            'font-size': '14px',
            'shape': 'circle',
            'border-opacity': 0.5,
            'background-opacity': 1
        }
    },
    {
        'selector': 'edge',
        'style': {
            # 'line-color': edge_line_color,  # Use the line color you defined
            'line-fill': 'linear-gradient',
            'line-gradient-stop-colors': '#8d6268 #c28d75',
            'line-gradient-stop-positions': '0% 100%',
            'width': '5px',  # Set the edge thickness
            'line-style': 'solid',  # Optional: 'solid', 'dashed', 'dotted', etc.
            'curve-style': 'bezier',  # Optional: 'bezier', 'straight', etc.
            # Optional Arrowhead Styling
            'target-arrow-shape': 'circle',
            'target-arrow-color': target_arrow_color,
            'arrow-scale': .75,  # Adjust arrow size as needed,
            'z-index': 2
        }
    },
]

cyto_component = cyto.Cytoscape(
    id='cytoscape',
    layout={'name': 'dagre', 'spacingFactor': 1},
    style={'height': '68vh',
           'width': '100%',
           'backgroundColor': cytoscape_background_color,
           'border': '15px solid #5d6872',
           'borderRadius': '30px',
           'box-shadow': 'inset 0px 0px 40px 40px #433455'},
    elements=default_elements,
    stylesheet=stylesheet
)
