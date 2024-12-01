from dash import Input, Output, State
from app_instance import app


@app.callback(
    [
        Output('custom1_input', 'style'),
        Output('custom2_input', 'style'),
        Output('custom3_input', 'style'),
        Output('custom1_input', 'placeholder'),
        Output('custom2_input', 'placeholder'),
        Output('custom3_input', 'placeholder'),
    ],
    Input('cytoscape', 'selectedNodeData'),
    State('field-values-button', 'active'),
)
def manage_inputs(selected, values_active):
    show = {'display': 'block'}
    hide = {'display': 'hide'}
    default_placeholder = 'Enter for entire tree'
    if not values_active:
        return show, show, show, default_placeholder, default_placeholder, default_placeholder
    else:
        if not selected:
            return hide, hide, hide, '', '', ''
        else:
            label = selected['data']['label']
            placeholder = 'Enter for ' + label
            return show, show, show, placeholder, placeholder, placeholder
