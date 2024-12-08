from dash import callback, Input, Output, State, exceptions, dcc
import json

@callback(
    Output('local-download', 'data'),
    Input('local-save-button', 'n_clicks'),
    [
        # color buttons
        State('blueberry-button', 'active'),
        State('banana-button', 'active'),
        State('grape-button', 'active'),
        State('orange-button', 'active'),

        # shape buttons
        State('circle-button', 'active'),
        State('triangle-button', 'active'),
        State('square-button', 'active'),
        State('octagon-button', 'active'),

        # outline buttons
        State('single-outline-button', 'active'),
        State('no-outline-button', 'active'),
        State('shadow-button', 'active'),
        State('double-button', 'active'),

        # pointer buttons
        State('circle-pointer-button', 'active'),
        State('no-pointer-button', 'active'),
        State('arrow-pointer-button', 'active'),
        State('tee-pointer-button', 'active'),

        # background buttons
        State('blue_background_button', 'active'),
        State('brown_background_button', 'active'),
        State('green_background_button', 'active'),
        State('black_background_button', 'active'),

        # Other states
        State('local-save-input', 'value'),
        State('author-input', 'value'),
        State('description-input', 'value'),
        State('cytoscape', 'elements'),
        State('file-info', 'data'),
    ],
    prevent_initial_call=True
)
def local_save(
    save_clicks,
    blueberry_active, banana_active, grape_active, orange_active,
    circle_active, triangle_active, square_active, octagon_active,
    single_outline_active, no_outline_active, shadow_outline_active, double_outline_active,
    circle_pointer_active, no_pointer_active, arrow_pointer_active, tee_pointer_active,
    blue_background_active, brown_background_active, green_background_active, black_background_active,
    file_name, author, description, current_tree, file_info
):

    if not save_clicks:
        raise exceptions.PreventUpdate

    # Determine filename
    if not file_name:
        file_name = 'DAG_tree'
    file_name += '.json'

    # Build the theme_data dictionary by checking which button is active in each category
    theme_data = {}

    # Colors
    if blueberry_active:
        theme_data['color'] = 'blueberry'
    elif banana_active:
        theme_data['color'] = 'banana'
    elif grape_active:
        theme_data['color'] = 'grape'
    elif orange_active:
        theme_data['color'] = 'orange'

    # Shapes
    if circle_active:
        theme_data['shape'] = 'circle'
    elif triangle_active:
        theme_data['shape'] = 'triangle'
    elif square_active:
        theme_data['shape'] = 'square'
    elif octagon_active:
        theme_data['shape'] = 'octagon'

    # Outlines
    if single_outline_active:
        theme_data['outline'] = 'single'
    elif no_outline_active:
        theme_data['outline'] = 'no-outline'
    elif shadow_outline_active:
        theme_data['outline'] = 'shadow'
    elif double_outline_active:
        theme_data['outline'] = 'double'

    # Pointers
    if circle_pointer_active:
        theme_data['pointer'] = 'circle'
    elif no_pointer_active:
        theme_data['pointer'] = 'no'
    elif arrow_pointer_active:
        theme_data['pointer'] = 'arrow'
    elif tee_pointer_active:
        theme_data['pointer'] = 'tee'

    # Background
    if blue_background_active:
        theme_data['background'] = 'blue'
    elif brown_background_active:
        theme_data['background'] = 'brown'
    elif green_background_active:
        theme_data['background'] = 'green'
    elif black_background_active:
        theme_data['background'] = 'black'

    # Construct the full dictionary with metadata and theme_data
    output_dict = {
        "Name": file_name,
        "Description": description,
        "Author": author,
        "theme_data": theme_data,
        "elements": current_tree if current_tree else []
    }

    content = json.dumps(output_dict, indent=2)

    return dcc.send_string(content, filename=file_name)
