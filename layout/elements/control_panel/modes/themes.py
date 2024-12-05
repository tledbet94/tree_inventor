from dash import dcc, Input, html, Output
import dash_bootstrap_components as dbc
from app_instance import app

themes_title = html.H1('Themes', className='edit-header-text')

# Color
color_label = html.P('Node Color', className='fields-label')

blueberry_button = dbc.Button(
    id='blueberry-button',
    children=html.Img(
        src="/assets/blueberry.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "60px",  # Adjust the height
            "width": "60px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

banana_button = dbc.Button(
    id='banana-button',
    children=html.Img(
        src="/assets/banana.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

grape_button = dbc.Button(
    id='grape-button',
    children=html.Img(
        src="/assets/grape.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

orange_button = dbc.Button(
    id='orange-button',
    children=html.Img(
        src="/assets/orange.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

# Node shape button
shape_label = html.P('Node Shape', className='fields-label')

circle_button = dbc.Button(
    id='circle-button',
    children=html.Img(
        src="/assets/button_icons/sphere.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

triangle_button = dbc.Button(
    id='triangle-button',
    children=html.Img(
        src="/assets/button_icons/star.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

square_button = dbc.Button(
    id='square-button',
    children=html.Img(
        src="/assets/button_icons/cube.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

octagon_button = dbc.Button(
    id='octagon-button',
    children=html.Img(
        src="/assets/button_icons/octagon.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

# Node Outline button
outline_label = html.P('Node Outline', className='fields-label')

single_outline_button = dbc.Button(
    id='single-outline-button',
    children=html.Img(
        src="/assets/button_icons/single_outline.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

no_outline_button = dbc.Button(
    id='no-outline-button',
    children='',
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

shadow_outline_button = dbc.Button(
    id='shadow-button',
    children=html.Img(
        src="/assets/button_icons/shadow_outline.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

double_outline_button = dbc.Button(
    id='double-button',
    children=html.Img(
        src="/assets/button_icons/double_outline.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

# Edge pointer
pointer_label = html.P('Pointer', className='fields-label')

circle_pointer_button = dbc.Button(
    id='circle-pointer-button',
    children=html.Img(
        src="/assets/button_icons/circle_pointer.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

no_pointer_button = dbc.Button(
    id='no-pointer-button',
    children="",
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

arrow_pointer_button = dbc.Button(
    id='arrow-pointer-button',
    children=html.Img(
        src="/assets/button_icons/arrow_pointer.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

tee_pointer_button = dbc.Button(
    id='tee-pointer-button',
    children=html.Img(
        src="/assets/button_icons/tee_pointer.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

# background buttons

background_label = html.P('Background', className='fields-label')

blue_background_button = dbc.Button(
    id='blue_background_button',
    children=html.Img(
        src="/assets/button_icons/blue_background.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

brown_background_button = dbc.Button(
    id='brown_background_button',
    children=html.Img(
        src="/assets/button_icons/brown_background.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

green_background_button = dbc.Button(
    id='green_background_button',
    children=html.Img(
        src="/assets/button_icons/green_background.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

black_background_button = dbc.Button(
    id='black_background_button',
    children=html.Img(
        src="/assets/button_icons/black_background.png",  # Path to the image
        className="pixel-art",
        style={
            "height": "50px",  # Adjust the height
            "width": "50px",  # Adjust the width
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

# styled row
color_row = dbc.Row([dbc.Col(blueberry_button), dbc.Col(banana_button), dbc.Col(grape_button),
                     dbc.Col(orange_button)],
                    className='themes-row')

shape_row = dbc.Row([dbc.Col(circle_button), dbc.Col(triangle_button),
                     dbc.Col(square_button), dbc.Col(octagon_button)],
                    className='themes-row')

outline_row = dbc.Row([dbc.Col(single_outline_button), dbc.Col(no_outline_button),
                       dbc.Col(shadow_outline_button),
                       dbc.Col(double_outline_button)],
                      className='themes-row')

pointer_row = dbc.Row([dbc.Col(circle_pointer_button), dbc.Col(no_pointer_button),
                       dbc.Col(arrow_pointer_button),
                       dbc.Col(tee_pointer_button)],
                      className='themes-row')

background_row = dbc.Row([dbc.Col(blue_background_button), dbc.Col(brown_background_button),
                          dbc.Col(green_background_button),
                          dbc.Col(black_background_button)],
                         className='themes-row')

themes = html.Div(
    [
        dbc.Row(dbc.Col(color_label)),
        color_row,
        html.Div(style={'height': '2vw'}),
        dbc.Row(dbc.Col(shape_label)),
        shape_row,
        html.Div(style={'height': '2vw'}),
        dbc.Row(dbc.Col(outline_label)),
        outline_row,
        html.Div(style={'height': '2vw'}),
        dbc.Row(dbc.Col(pointer_label)),
        pointer_row,
        html.Div(style={'height': '2vw'}),
        dbc.Row(dbc.Col(background_label)),
        background_row
    ]
)
