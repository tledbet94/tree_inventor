import dash_cytoscape as cyto

# Internal imports
from .elements import default_elements

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
            'border-width': '4px',
            'border-color': node_border_color,
            'border-style': 'solid',
            'label': 'data(label)',
            'text-valign': 'center',
            'text-halign': 'center',
            'color': '#f2f0e5',
            'font-size': '14px',
            'shape': 'circle',
            'border-opacity': 0.75,
            'background-opacity': 1
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
            'target-arrow-color': '#68c2d3',
            'arrow-scale': .75,  # Adjust arrow size as needed,
            'z-index': 2,
            'opacity': 0.9,

        }
    },
]

cyto_component = cyto.Cytoscape(
    id='cytoscape',
    layout={'name': 'dagre', 'spacingFactor': 1},
    style={'height': '68vh',
           'width': '100%',
           'backgroundColor': cytoscape_background_color,
           'border': '15px solid #868188',
           'borderRadius': '30px',
           'box-shadow': 'inset 0px 0px 10px 10px #646365'},
    elements=default_elements,
    stylesheet=stylesheet
)
