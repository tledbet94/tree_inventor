import base64
import json
from dash import callback, ctx, Input, Output, State, exceptions, dcc



@callback(
    Output('file-info', 'data'),
    [
        Input('upload-area', 'contents'),
        Input('template_one_button', 'active'),
        Input('template_two_button', 'active'),
        Input('template_three_button', 'active'),
        Input('template_four_button', 'active'),
        Input('template_five_button', 'active'),
        Input('template_six_button', 'active'),
        Input('template_seven_button', 'active'),
        Input('template_eight_button', 'active'),
    ],
    [
        State('cytoscape', 'elements'),
        State('file-info', 'data'),
        State('upload-active', 'data')
    ]
)
def update_file_info(uploaded_json, active_one, active_two, active_three, active_four,
                     active_five, active_six, active_seven, active_eight,
                     previous_elements, previous_file_info, upload_active):
    if ctx.triggered_id == 'upload-area' and uploaded_json is not None:
        # The uploaded_json is a base64 data URL: data:application/json;base64,<BASE64_DATA>
        content_type, content_string = uploaded_json.split(',')
        decoded = base64.b64decode(content_string)

        try:
            loaded_elements = json.loads(decoded.decode('utf-8'))
        except Exception as e:
            print("Error reading uploaded JSON:", e)
            # If parsing fails, return previous_file_info or some fallback
            return previous_file_info

        name = loaded_elements.get('Name', '')
        description = loaded_elements.get('Description', '')
        author = loaded_elements.get('Author', '')
        theme_data = loaded_elements.get('theme_data', '')

        file_info = {
            'Name': name,
            'Description': description,
            'Author': author,
            'theme_data': theme_data
        }
        return file_info

    elif not upload_active:
        # Handle the template selection
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

        current_tree = template_files[1]
        if active_one:
            current_tree = template_files[1]
        elif active_two:
            current_tree = template_files[2]
        elif active_three:
            current_tree = template_files[3]
        elif active_four:
            current_tree = template_files[4]
        elif active_five:
            current_tree = template_files[5]
        elif active_six:
            current_tree = template_files[6]
        elif active_seven:
            current_tree = template_files[7]
        elif active_eight:
            current_tree = template_files[8]

        with open(current_tree, "r") as json_file:
            loaded_elements = json.load(json_file)
            name = loaded_elements.get('Name', '')
            description = loaded_elements.get('Description', '')
            author = loaded_elements.get('Author', '')
            theme_data = loaded_elements.get('theme_data', '')

            file_info = {
                'Name': name,
                'Description': description,
                'Author': author,
                'theme_data': theme_data
            }
            return file_info
    else:
        return previous_file_info
