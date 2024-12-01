from dash import Input, Output, State
from app_instance import app


@app.callback(
    [
        Output('custom1_label', 'style'),
        Output('custom2_label', 'style'),
        Output('custom3_label', 'style'),
        Output('custom1_input', 'style'),
        Output('custom2_input', 'style'),
        Output('custom3_input', 'style'),
        Output('custom-update-button', 'style'),
        Output('custom1_input', 'placeholder'),
        Output('custom2_input', 'placeholder'),
        Output('custom3_input', 'placeholder'),
    ],
    Input('cytoscape', 'selectedNodeData'),
    Input('field-names-button', 'active'),
    Input('field-values-button', 'active'),
    Input('custom-fields-button', 'active'),
)
def manage_inputs(selected, names_active, values_active, fields_active):
    show = {'display': 'block'}
    hide = {'display': 'none'}
    default_placeholder = 'Enter for entire tree'
    if not values_active:
        return (show, show, show, show, show, show, show,
                default_placeholder, default_placeholder, default_placeholder)
    else:
        if not selected:
            return (hide, hide, hide, hide, hide, hide, hide,
                    '', '', '')
        else:
            placeholder = 'Enter for selected node'
            return (show, show, show, show, show, show, show,
                    placeholder, placeholder, placeholder)
