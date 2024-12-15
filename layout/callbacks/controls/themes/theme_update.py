from dash import callback, Input, Output, State, callback_context


@callback(
    [
        Output('cytoscape', 'stylesheet'),
        Output('cytoscape', 'style')
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
)
def theme_update(blueberry_color_active, banana_color_active, grape_color_active, orange_color_active,
                 circle_shape_active, triangle_shape_active, square_shape_active, octagon_shape_active,
                 single_outline_active, no_outline_active, shadow_outline_active, double_outline_active,
                 circle_pointer_active, no_pointer_active, arrow_pointer_active, tee_pointer_active,
                 blue_background_active, brown_background_active, green_background_active, black_background_active,
                 current_cyto_style, background_style):
    # Color
    print('theme_update')
    if blueberry_color_active:
        current_cyto_style[0]['style']['background-color'] = '#4b80ca'
        current_cyto_style[0]['style']['border-color'] = '#68c2d3'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#43436a #4b80ca'
        current_cyto_style[2]['style']['target-arrow-color'] = '#a2dcc7'
    elif banana_color_active:
        current_cyto_style[0]['style']['background-color'] = '#feae34'
        current_cyto_style[0]['style']['border-color'] = '#fee761'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#ead4aa #feae34'
        current_cyto_style[2]['style']['target-arrow-color'] = '#ead4aa'
    elif grape_color_active:
        current_cyto_style[0]['style']['background-color'] = '#564064'
        current_cyto_style[0]['style']['border-color'] = '#8e478c'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#564064 #cd6093'
        current_cyto_style[2]['style']['target-arrow-color'] = '#ffaeb6'
    elif orange_color_active:
        current_cyto_style[0]['style']['background-color'] = '#f1892d'
        current_cyto_style[0]['style']['border-color'] = '#ffd19d'
        current_cyto_style[2]['style']['line-gradient-stop-colors'] = '#ffd19d #f1892d'
        current_cyto_style[2]['style']['target-arrow-color'] = '#ffd19d'


    # Shape
    if circle_shape_active:
        current_cyto_style[0]['style']['shape'] = 'circle'
    elif triangle_shape_active:
        current_cyto_style[0]['style']['shape'] = 'triangle'
    elif square_shape_active:
        current_cyto_style[0]['style']['shape'] = 'square'
    elif octagon_shape_active:
        current_cyto_style[0]['style']['shape'] = 'octagon'

    # Outline
    if single_outline_active:
        current_cyto_style[0]['style']['border-style'] = 'solid'
        current_cyto_style[0]['style']['border-opacity'] = '1'
        current_cyto_style[0]['style']['border-width'] = '4vh'
    elif no_outline_active:
        current_cyto_style[0]['style']['border-width'] = '0vh'
    elif shadow_outline_active:
        # this style will use multiple effects
        current_cyto_style[0]['style']['border-style'] = 'ridge'
        current_cyto_style[0]['style']['border-opacity'] = '0.5'
        current_cyto_style[0]['style']['border-width'] = '12vh'

    elif double_outline_active:
        current_cyto_style[0]['style']['border-style'] = 'double'
        current_cyto_style[0]['style']['border-opacity'] = '.75'
        current_cyto_style[0]['style']['border-width'] = '8vh'

    # Pointer
    if circle_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'circle'
    elif no_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'none'
    elif arrow_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'triangle'
    elif tee_pointer_active:
        current_cyto_style[2]['style']['target-arrow-shape'] = 'tee'

    # Background
    if blue_background_active:
        background_style['backgroundColor'] = '#352b42'
    elif brown_background_active:
        background_style['backgroundColor'] = '#3f2832'
    elif green_background_active:
        background_style['backgroundColor'] = '#302c2e'
    elif black_background_active:
        background_style['backgroundColor'] = '#100820'

    return current_cyto_style, background_style
