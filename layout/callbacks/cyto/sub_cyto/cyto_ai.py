import os
import json
import dash
from dash import dcc, html, callback, ctx, Input, Output, State, no_update
import dash_cytoscape as cyto
import openai
import traceback

# Retrieve your API key from an environment variable (preferred).
openai.api_key = os.getenv("OPENAI_API_KEY")

# Example reference tree to show the model what JSON structure to return
reference_tree_json = {
    "Name": "Example Tree",
    "Description": "Simple JSON structure for demonstration",
    "Author": "AI",
    "theme_data": {
        "color": "blue",
        "shape": "circle",
        "outline": "single-outline",
        "pointer": "circle-pointer",
        "background": "blue-background"
    },
    "elements": [
        {
            "data": {
                "id": "root",
                "label": "ROOT_NODE",
                "weight": 0,
                "level": 1,
                "children": 0,
                "traversed": "False",
                "common": "False",
                "invalid_weight": "False",
                "last_clicked": "False",
                "custom1": {"field_name": "Field1", "field_value": ""},
                "custom2": {"field_name": "Field2", "field_value": ""},
                "custom3": {"field_name": "Field3", "field_value": ""}
            },
            "position": {"x": 100, "y": 100}
        }
    ]
}

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Textarea(
        id='ai-input',
        value='',
        placeholder='Enter your topic or instructions here...',
        style={'width': '100%', 'height': 100},
    ),
    html.Button("Generate Tree", id='ai-update-button'),
    html.Div(id='ai-elements', style={'whiteSpace': 'pre-wrap', 'marginTop': '20px'}),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[],
        style={'width': '100%', 'height': '400px', 'border': '1px solid #ccc'}
    )
])


@callback(
    Output('ai-elements', 'data'),  # We'll store the raw JSON result here
    [
        Input('ai-update-button', 'n_clicks'),
        Input('ai-expand-button', 'n_clicks')
    ],
    [
        State('ai-input', 'value'),
        State('cytoscape', 'tapNode'),
        State('cytoscape', 'elements')
    ],
    prevent_initial_call=True
)
def ai_summon(update_clicks, expand_clicks, user_prompt, tap_node, current_elements):
    """
    Sends the user's topic + reference JSON to the new openai.Chat endpoint.
    Then parses the response as JSON and returns 'elements' to the Dash component.
    """
    print("\n---- ai_summon callback triggered ----")
    print("DEBUG: Number of clicks ->", update_clicks)
    print("DEBUG: User prompt ->", user_prompt)

    prompt = user_prompt
    starting_point = 'root'
    if tap_node:
        starting_point = tap_node['data']['id']
    ai_task = 'update'
    if ctx.triggered_id == 'ai-update-button':
        ai_task = 'update'
    elif ctx.triggered_id == 'ai-expand-button':
        ai_task = 'expand'
        prompt = ('Current tree' + str(current_elements) + 'Task: ' +
                  ai_task + ' ' + user_prompt + ' Starting Point ' + starting_point)

    if user_prompt is None or '':
        return current_elements

    # Build a minimal prompt
    # 'developer' role is the new 'system' role per latest docs.
    # 'user' is the specific request. We also embed reference JSON.
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You produce JSON trees in a directed acyclic graph structure.\n\n"
                        "Constraints:\n"
                        "1) Output MUST follow the JSON schema exactly—no extra keys.\n"
                        "2) All nodes must have at least one edge except for the root.\n"
                        "3) All edges must have data.source, data.target, and weight > 0.\n"
                        "4) Position data must exist for nodes.\n"
                        "5) No markdown in the output.\n\n"
    
                        "Behavior:\n"
                        "- If ai_task='expand', build a larger tree from existing tree"
                        "Instead, add nodes/edges from the 'starting_point' node.\n"
                        "- Return valid JSON only.\n"
                    )
                },
                {"role": "user",
                 "content": prompt},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "my_custom_tree_schema",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "Name": {"type": "string"},
                            "Description": {"type": "string"},
                            "Author": {"type": "string"},
                            "theme_data": {
                                "type": "object",
                                "properties": {
                                    "color": {"type": "string"},
                                    "shape": {"type": "string"},
                                    "outline": {"type": "string"},
                                    "pointer": {"type": "string"},
                                    "background": {"type": "string"}
                                },
                                "required": [
                                    "color", "shape", "outline",
                                    "pointer", "background"
                                ],
                                "additionalProperties": False
                            },
                            "elements": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "oneOf": [
                                        {
                                            # Node schema
                                            "properties": {
                                                "data": {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {"type": "string"},
                                                        "label": {"type": "string"},
                                                        "weight": {"type": "number"},
                                                        "level": {"type": "number"},
                                                        "children": {"type": "number"},
                                                        "traversed": {"type": "string"},
                                                        "common": {"type": "string"},
                                                        "invalid_weight": {"type": "string"},
                                                        "last_clicked": {"type": "string"},
                                                        "custom1": {
                                                            "type": "object",
                                                            "properties": {
                                                                "field_name": {"type": "string"},
                                                                "field_value": {"type": "string"}
                                                            },
                                                            "required": ["field_name", "field_value"],
                                                            "additionalProperties": False
                                                        },
                                                        "custom2": {
                                                            "type": "object",
                                                            "properties": {
                                                                "field_name": {"type": "string"},
                                                                "field_value": {"type": "string"}
                                                            },
                                                            "required": ["field_name", "field_value"],
                                                            "additionalProperties": False
                                                        },
                                                        "custom3": {
                                                            "type": "object",
                                                            "properties": {
                                                                "field_name": {"type": "string"},
                                                                "field_value": {"type": "string"}
                                                            },
                                                            "required": ["field_name", "field_value"],
                                                            "additionalProperties": False
                                                        }
                                                    },
                                                    "required": [
                                                        "id", "label", "weight", "level",
                                                        "children", "traversed", "common",
                                                        "invalid_weight", "last_clicked",
                                                        "custom1", "custom2", "custom3"
                                                    ],
                                                    "additionalProperties": False
                                                },
                                                "position": {
                                                    "type": "object",
                                                    "properties": {
                                                        "x": {"type": "number"},
                                                        "y": {"type": "number"}
                                                    },
                                                    "required": ["x", "y"],
                                                    "additionalProperties": False
                                                }
                                            },
                                            "required": ["data", "position"],
                                            "additionalProperties": False
                                        },
                                        {
                                            # Edge schema
                                            "properties": {
                                                "data": {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {"type": "string"},
                                                        "source": {"type": "string"},  # Edge source node
                                                        "target": {"type": "string"},  # Edge target node
                                                        "weight": {"type": "number", "minimum": 0.0001},  # Weight > 0
                                                        "traversed": {"type": "string"},
                                                        "last_clicked": {"type": "string"}
                                                    },
                                                    "required": ["id", "source", "target", "weight"],
                                                    "additionalProperties": False
                                                }
                                            },
                                            "required": ["data"],
                                            "additionalProperties": False
                                        }
                                    ]
                                }
                            }
                        },
                        "required": [
                            "Name", "Description", "Author",
                            "theme_data", "elements"
                        ],
                        "additionalProperties": False
                    }
                }
            }

        )

        ai_output = response.choices[0].message.content
        print(ai_output)
        json_data = json.loads(ai_output)
        json_data = json_data['elements']
        return json_data

    except Exception as e:
            print("Error in callback:")
            print(traceback.format_exc())
            return no_update