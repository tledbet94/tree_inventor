from dash import Input, Output, State
from app_instance import app
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


@app.callback(
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
    ],
    [
        Input('custom-update-button', 'n_clicks'),
        Input('cytoscape', 'tapNode')
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
        State('cytoscape', 'elements')
    ]
)
def fields_update(update_clicks, tap_node,
                  names_active, values_active, custom1_input, custom2_input, custom3_input,
                  elements):
    elements = copy.deepcopy(elements) if elements is not None else []
    name1 = ''
    name2 = ''
    name3 = ''

    # Identify the selected node
    selected_node_id = None
    if tap_node:
        selected_node_id = tap_node['data']['id']

    # Update custom field names
    if names_active and elements and update_clicks and update_clicks > 0:
        for element in elements:
            if 'source' not in element['data'] and element['data'].get('id') == selected_node_id:
                if custom1_input not in (None, ''):
                    element['data']['custom1']['field_name'] = custom1_input
                else:
                    custom1_input = element['data']['custom1']['field_name']
                if custom2_input not in (None, ''):
                    element['data']['custom2']['field_name'] = custom2_input
                else:
                    custom2_input = element['data']['custom2']['field_name']
                if custom3_input not in (None, ''):
                    element['data']['custom3']['field_name'] = custom3_input
                else:
                    custom3_input = element['data']['custom3']['field_name']
                value1, value2, value3 = get_node_values(elements, selected_node_id)
                return elements, '', '', '', custom1_input, custom2_input, custom3_input, custom1_input, custom2_input, custom3_input, value1, value2, value3

    # Update custom field values
    elif values_active and elements and update_clicks and update_clicks > 0:
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
                name1 = element['data']['custom1']['field_name']
                name2 = element['data']['custom2']['field_name']
                name3 = element['data']['custom3']['field_name']
                value1, value2, value3 = get_node_values(elements, selected_node_id)
                return elements, '', '', '', name1, name2, name3, name1, name2, name3, value1, value2, value3

    # Default case: update labels based on the selected node
    else:
        if elements and selected_node_id:
            for element in elements:
                if 'source' not in element['data'] and element['data'].get('id') == selected_node_id:
                    name1 = element['data']['custom1']['field_name']
                    name2 = element['data']['custom2']['field_name']
                    name3 = element['data']['custom3']['field_name']
                    break

    value1, value2, value3 = get_node_values(elements, selected_node_id)
    return elements, '', '', '', name1, name2, name3, name1, name2, name3, value1, value2, value3
