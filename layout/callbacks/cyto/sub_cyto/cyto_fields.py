from dash import callback, ctx, Input, Output, State
import copy


def get_node_values(elements, node_id):
    field_one = ''
    field_two = ''
    field_three = ''
    for e in elements:
        if node_id == e['data']['id']:
            field_one = e['data']['custom1']['field_value']
            field_two = e['data']['custom2']['field_value']
            field_three = e['data']['custom3']['field_value']
    return field_one, field_two, field_three


@callback(
    [
        Output('fields-store', 'data'),
        # Custom field inputs
        Output('custom1_input', 'value'),
        Output('custom2_input', 'value'),
        Output('custom3_input', 'value'),
        # custom field panel labels
        Output('custom1_label', 'children'),
        Output('custom2_label', 'children'),
        Output('custom3_label', 'children'),
        # info panel labels
        Output('info-custom1-label', 'children'),
        Output('info-custom2-label', 'children'),
        Output('info-custom3-label', 'children'),
        # info panel values
        Output('node-custom1', 'children'),
        Output('node-custom2', 'children'),
        Output('node-custom3', 'children'),
        Output('field-names-store', 'data')
    ],
    [
        Input('custom-update-button', 'n_clicks'),
        Input('cytoscape', 'tapNode'),
        Input('template-store', 'data')
    ],
    [
        # check which mode is active - names or values
        State('field-names-button', 'active'),
        State('field-values-button', 'active'),
        # get from inputs
        State('custom1_input', 'value'),
        State('custom2_input', 'value'),
        State('custom3_input', 'value'),
        # need to make copy of elements initially
        State('cytoscape', 'elements'),
        State('field-names-store', 'data')
    ]
)
def fields_update(update_clicks, tap_node, template_elements,
                  names_active, values_active, custom1_input, custom2_input, custom3_input,
                  elements, stored_names):

    # Make an independent copy and then serve the changes back later
    elements = copy.deepcopy(elements) if elements is not None else []

    trigger_id = ctx.triggered_id

    # When app starts, initialize with the field names of the current tree
    if stored_names == ['', '', '']:
        for element in elements:
            if 'custom1' in element['data']:
                stored_names[0] = element['data']['custom1']['field_name']
                stored_names[1] = element['data']['custom2']['field_name']
                stored_names[2] = element['data']['custom3']['field_name']

    if trigger_id == 'template-store':
        for element in template_elements:
            if 'custom1' in element['data']:
                stored_names[0] = element['data']['custom1']['field_name']
                stored_names[1] = element['data']['custom2']['field_name']
                stored_names[2] = element['data']['custom3']['field_name']

    # Identify the selected node
    selected_node_id = None
    if tap_node:
        selected_node_id = tap_node['data']['id']

    # Update custom field names
    if names_active and trigger_id == 'custom-update-button':
        for element in elements:
            if 'source' not in element['data']:
                if custom1_input not in (None, ''):
                    element['data']['custom1']['field_name'] = custom1_input
                    stored_names[0] = custom1_input  # Update stored_names
                else:
                    custom1_input = stored_names[0]
                if custom2_input not in (None, ''):
                    element['data']['custom2']['field_name'] = custom2_input
                    stored_names[1] = custom2_input  # Update stored_names
                else:
                    custom2_input = stored_names[1]
                if custom3_input not in (None, ''):
                    element['data']['custom3']['field_name'] = custom3_input
                    stored_names[2] = custom3_input  # Update stored_names
                else:
                    custom3_input = stored_names[2]
                value1, value2, value3 = get_node_values(elements, selected_node_id)
                names_list = [custom1_input, custom2_input, custom3_input]
                return (elements, '', '', '', custom1_input, custom2_input, custom3_input,
                        custom1_input, custom2_input, custom3_input,
                        value1, value2, value3, stored_names)

    # Update custom field values
    elif values_active and trigger_id == 'custom-update-button':  # Corrected condition
        for element in elements:
            if 'source' not in element['data'] and element['data'].get('id') == selected_node_id:
                if custom1_input not in (None, ''):
                    element['data']['custom1']['field_value'] = custom1_input
                else:
                    custom1_input = element['data']['custom1']['field_value']
                if custom2_input not in (None, ''):
                    element['data']['custom2']['field_value'] = custom2_input
                else:
                    custom2_input = element['data']['custom2']['field_value']
                if custom3_input not in (None, ''):
                    element['data']['custom3']['field_value'] = custom3_input
                else:
                    custom3_input = element['data']['custom3']['field_value']
                name1 = stored_names[0]
                name2 = stored_names[1]
                name3 = stored_names[2]
                value1, value2, value3 = get_node_values(elements, selected_node_id)
                return (elements, '', '', '', name1, name2, name3,
                        name1, name2, name3,
                        value1, value2, value3, stored_names)

    name1 = stored_names[0]
    name2 = stored_names[1]
    name3 = stored_names[2]

    value1, value2, value3 = get_node_values(elements, selected_node_id)
    return elements, '', '', '', name1, name2, name3, name1, name2, name3, value1, value2, value3, stored_names
