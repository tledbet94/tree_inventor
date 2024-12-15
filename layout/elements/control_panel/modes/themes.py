from dash import dcc, Input, html, Output
import dash_bootstrap_components as dbc

themes_title = html.H1('Themes', className='edit-header-text')

# Color
color_label = html.P('Node Color', className='fields-label')

blueberry_button = dbc.Button(
    id='blueberry-button',
    children=html.Img(
        src="/assets/blueberry.png",  # Path to the image
        className="pixel-art",
        style={
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
            "verticalAlign": "middle",  # Center the image vertically within the button
        }
    ),
    className="theme-button",
    style={'outline': 'none'},
    disabled=False,
)

# styled row
color_row = dbc.Row(
    [
        dbc.Col(blueberry_button, width=3),
        dbc.Col(banana_button, width=3),
        dbc.Col(grape_button, width=3),
        dbc.Col(orange_button, width=3),
    ],
    className='themes-row',
    justify='center',  # Center the buttons
    style={"flex-wrap": "nowrap"},  # Prevent wrapping
)

shape_row = dbc.Row(
    [
        dbc.Col(circle_button, width=3),
        dbc.Col(triangle_button, width=3),
        dbc.Col(square_button, width=3),
        dbc.Col(octagon_button, width=3),
    ],
    className='themes-row',
    justify='center',
    style={"flex-wrap": "nowrap"},
)

outline_row = dbc.Row(
    [
        dbc.Col(single_outline_button, width=3),
        dbc.Col(no_outline_button, width=3),
        dbc.Col(shadow_outline_button, width=3),
        dbc.Col(double_outline_button, width=3),
    ],
    className='themes-row',
    justify='center',
    style={"flex-wrap": "nowrap"},
)

pointer_row = dbc.Row(
    [
        dbc.Col(circle_pointer_button, width=3),
        dbc.Col(no_pointer_button, width=3),
        dbc.Col(arrow_pointer_button, width=3),
        dbc.Col(tee_pointer_button, width=3),
    ],
    className='themes-row',
    justify='center',
    style={"flex-wrap": "nowrap"},
)

background_row = dbc.Row(
    [
        dbc.Col(blue_background_button, width=3),
        dbc.Col(brown_background_button, width=3),
        dbc.Col(green_background_button, width=3),
        dbc.Col(black_background_button, width=3),
    ],
    className='themes-row',
    justify='center',
    style={"flex-wrap": "nowrap"},
)

themes = html.Div(
    [
        dbc.Row(dbc.Col(color_label)),
        color_row,
        html.Div(className='theme-spacer'),
        dbc.Row(dbc.Col(shape_label)),
        shape_row,
        html.Div(className='theme-spacer'),
        dbc.Row(dbc.Col(outline_label)),
        outline_row,
        html.Div(className='theme-spacer'),
        dbc.Row(dbc.Col(pointer_label)),
        pointer_row,
        html.Div(className='theme-spacer'),
        dbc.Row(dbc.Col(background_label)),
        background_row
    ]
)
