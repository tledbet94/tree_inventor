from dash import callback, Input, Output, State
import base64
import json


@callback(
    Output('upload-store', 'data'),
    Output('upload-active', 'data'),
    Input('upload-area', 'contents'),
    State('cytoscape', 'elements')
)
def upload_tree(contents, previous_elements):
    if contents is not None:
        # contents is a string: "data:application/json;base64,<BASE64_STRING>"
        content_type, content_string = contents.split(',')

        # Decode the Base64 string
        decoded = base64.b64decode(content_string)

        try:
            # Convert the decoded bytes to a string and load the JSON
            loaded_data = json.loads(decoded.decode('utf-8'))
            elements = loaded_data.get('elements', previous_elements)
            return elements, True
        except Exception as e:
            print("Error loading JSON:", e)
            return previous_elements, False
    else:
        return previous_elements, False
