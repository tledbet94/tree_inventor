from dash import Input, Output, State
from app_instance import app
import copy


# update elements through this call back - info_panel and the labels in custom fields should update based on elements
@app.callback(
    [
        # pathway to update elements
        Output('fields-store', 'data'),
        # wipe inputs clean
        Output('custom1_input', 'value'),
        Output('custom2_input', 'value'),
        Output('custom3_input', 'value'),
        # update actual labels in custom field panels if needed
        Output('custom1_label', 'children'),
        Output('custom2_label', 'children'),
        Output('custom3_label', 'children'),
        # update info panel labels
        Output('custom1_label', 'children'),
        Output('custom2_label', 'children'),
        Output('custom3_label', 'children'),
    ],
    [
        Input('custom-update-button', 'n_clicks')
    ],
    [
        State('field-names-button', 'active'),
        State('field-values-button', 'active'),
        State('custom1_input', 'value'),
        State('custom2_input', 'value'),
        State('custom3_input', 'value'),
        State('cytoscape', 'elements')

    ]
)
def fields_update(update_clicks, names_active, values_active, custom1_input, custom2_input, custom3_input,
                  elements):
    elements = copy.deepcopy(elements) if elements else []
    # Names updates the actual Custom Field label names, vs values just updates values in the CFs
    # On names panel, get name inputs
    if names_active and elements and update_clicks:
        for element in elements:
            if 'source' not in element['data']:
                element['data']['custom1']['field_name'] = custom1_input
                element['data']['custom2']['field_name'] = custom2_input
                element['data']['custom3']['field_name'] = custom3_input

    # On values panel, get name inputs
    elif values_active and elements and update_clicks:
        for element in elements:
            if 'source' not in element['data']:
                element['data']['custom1']['field_value'] = custom1_input
                element['data']['custom2']['field_value'] = custom2_input
                element['data']['custom3']['field_value'] = custom3_input

    # If name or values update, will return through fields_elements
    # If neither names nor values is active what goes in comes out
    return elements, '', '', ''
