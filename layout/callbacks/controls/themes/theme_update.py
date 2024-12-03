from dash import Input, Output, State, callback_context
from app_instance import app


@app.callback(
    Output('cytoscape', 'stylesheet'),
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
        Input('tee-pointer-button', 'active')
    ]
)
def theme_update(blueberry_color_active, banana_color_active, grape_color_active, orange_color_active,
                 circle_shape_active, triangle_shape_active, square_shape_active, octagon_shape_active,
                 single_outline_active, no_outline_active, shadow_active, double_active,
                 circle_pointer_active, no_pointer_active, arrow_pointer_active, tee_pointer_active):
    pass
