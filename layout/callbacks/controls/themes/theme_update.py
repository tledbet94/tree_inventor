from dash import Input, Output, State, callback_context
from app_instance import app


@app.callback(
    [
        Output('cytoscape', 'stylesheet'),
        Output('cytoscape', 'style'),
        Output('file-info', 'data')
    ],
    [
        # color buttons
        Input('blueberry-button', 'active'),
        Input('banana-button', 'active'),
        Input('grape-button', 'active'),
        Input('orange-button', 'active'),
        # shape buttons
        Input('circle-button', 'active'),
        Input('triangle-button', 'active'),
        Input('square-button', 'active'),
        Input('octagon-button', 'active'),
        # outline buttons
        Input('single-outline-button', 'active'),
        Input('no-outline-button', 'active'),
        Input('shadow-button', 'active'),
        Input('double-button', 'active'),
        # pointer buttons
        Input('circle-pointer-button', 'active'),
        Input('no-pointer-button', 'active'),
        Input('arrow-pointer-button', 'active'),
        Input('tee-pointer-button', 'active'),
        # background buttons
        Input('blue_background_button', 'active'),
        Input('brown_background_button', 'active'),
        Input('green_background_button', 'active'),
        Input('black_background_button', 'active'),
    ],
    State('cytoscape', 'stylesheet'),
    State('cytoscape', 'style'),
    State('file-info', 'data')
)
def theme_update(blueberry_color_active, banana_color_active, grape_color_active, orange_color_active,
                 circle_shape_active, triangle_shape_active, square_shape_active, octagon_shape_active,
                 single_outline_active, no_outline_active, shadow_outline_active, double_outline_active,
                 circle_pointer_active, no_pointer_active, arrow_pointer_active, tee_pointer_active,
                 blue_background_active, brown_background_active, green_background_active, black_background_active,
                 current_cyto_style, background_style, file_info):
    # Color
    if blueberry_color_active:
        current_cyto_style[0]['style']['background-color'] = '#4b80ca'
        current_cyto_style[0]['style']['border-color'] = '#68c2d3'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#43436a #4b80ca'
        current_cyto_style[2]['style']['target-arrow-color'] = '#a2dcc7'
        file_info['theme_data']['color'] = 'blueberry'
    elif banana_color_active:
        current_cyto_style[0]['style']['background-color'] = '#feae34'
        current_cyto_style[0]['style']['border-color'] = '#fee761'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#ead4aa #feae34'
        current_cyto_style[2]['style']['target-arrow-color'] = '#ead4aa'
        file_info['theme_data']['color'] = 'banana'
    elif grape_color_active:
        current_cyto_style[0]['style']['background-color'] = '#564064'
        current_cyto_style[0]['style']['border-color'] = '#8e478c'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#564064 #cd6093'
        current_cyto_style[2]['style']['target-arrow-color'] = '#ffaeb6'
        file_info['theme_data']['color'] = 'grape'
    elif orange_color_active:
        current_cyto_style[0]['style']['background-color'] = '#f1892d'
        current_cyto_style[0]['style']['border-color'] = '#ffd19d'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#ffd19d #f1892d'
        current_cyto_style[2]['style']['target-arrow-color'] = '#ffd19d'
        file_info['theme_data']['color'] = 'orange'


    # Shape
    if circle_shape_active:
        current_cyto_style[0]['style']['shape'] = 'circle'
        file_info['theme_data']['shape'] = 'circle'
    elif triangle_shape_active:
        current_cyto_style[0]['style']['shape'] = 'triangle'
        file_info['theme_data']['shape'] = 'triangle'
    elif square_shape_active:
        current_cyto_style[0]['style']['shape'] = 'square'
        file_info['theme_data']['shape'] = 'square'
    elif octagon_shape_active:
        current_cyto_style[0]['style']['shape'] = 'octagon'
        file_info['theme_data']['shape'] = 'octagon'

    # Outline
    if single_outline_active:
        current_cyto_style[0]['style']['border-style'] = 'solid'
        current_cyto_style[0]['style']['border-opacity'] = '1'
        current_cyto_style[0]['style']['border-width'] = '4vh'
        file_info['theme_data']['outline'] = 'single'
    elif no_outline_active:
        current_cyto_style[0]['style']['border-width'] = '0vh'
        file_info['theme_data']['outline'] = 'no-outline'
    elif shadow_outline_active:
        # this style will use multiple effects
        current_cyto_style[0]['style']['border-style'] = 'ridge'
        current_cyto_style[0]['style']['border-opacity'] = '0.5'
        current_cyto_style[0]['style']['border-width'] = '12vh'
        file_info['theme_data']['outline'] = 'shadow'

    elif double_outline_active:
        current_cyto_style[0]['style']['border-style'] = 'double'
        current_cyto_style[0]['style']['border-opacity'] = '.75'
        current_cyto_style[0]['style']['border-width'] = '8vh'
        file_info['theme_data']['outline'] = 'double'

    # Pointer
    if circle_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'circle'
        file_info['theme_data']['pointer'] = 'circle'
    elif no_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'none'
        file_info['theme_data']['pointer'] = 'no'
    elif arrow_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'triangle'
        file_info['theme_data']['pointer'] = 'arrow'
    elif tee_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'tee'
        file_info['theme_data']['pointer'] = 'tee'

    # Background
    if blue_background_active:
        background_style['backgroundColor'] = '#352b42'
        file_info['theme_data']['background'] = 'blue'
    elif brown_background_active:
        background_style['backgroundColor'] = '#3f2832'
        file_info['theme_data']['background'] = 'brown'
    elif green_background_active:
        background_style['backgroundColor'] = '#302c2e'
        file_info['theme_data']['background'] = 'green'
    elif black_background_active:
        background_style['backgroundColor'] = '#100820'
        file_info['theme_data']['background'] = 'black'

    return current_cyto_style, background_style, file_info
