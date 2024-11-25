from dash import ctx, Input, Output, State
from app_instance import app

from cytoscape.templates.wake_up import default_elements as wake_up
from cytoscape.templates.two import default_elements as df2
from cytoscape.templates.three import default_elements as df3
from cytoscape.templates.four import default_elements as df4
from cytoscape.templates.five import default_elements as df5
from cytoscape.templates.six import default_elements as df6
from cytoscape.templates.seven import default_elements as df7
from cytoscape.templates.eight import default_elements as df8


@app.callback(
    Output('template-store', 'data'),
    [
        Input('template_one_button', 'active'),
        Input('template_two_button', 'active'),
        Input('template_three_button', 'active'),
        Input('template_four_button', 'active'),
        Input('template_five_button', 'active'),
        Input('template_six_button', 'active'),
        Input('template_seven_button', 'active'),
        Input('template_eight_button', 'active'),
    ],
    State('cytoscape', 'elements')
)
def swap_trees(one_active, two_active, three_active, four_active,
               five_active, six_active, seven_active, eight_active, current_elements):

    if one_active:
        return wake_up
    elif two_active:
        return df2
    elif three_active:
        return df3
    elif four_active:
        return df4
    elif five_active:
        return df5
    elif six_active:
        return df6
    elif seven_active:
        return df7
    elif eight_active:
        return df8
    else:
        return current_elements

