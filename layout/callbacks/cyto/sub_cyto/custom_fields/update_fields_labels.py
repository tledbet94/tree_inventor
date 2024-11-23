from dash import Input, Output, State
from app_instance import app
import copy


@app.callback(
    [
        Output('custom1_label', 'children'),
        Output('custom2_label', 'children'),
        Output('custom3_label', 'children'),
    ],
    Input('custom-fields-button', 'n_clicks'),
    State('fields-store', 'data'),
    State('cytoscape', 'elements')
)
def update_labels(custom_clicks, field_elements, elements):
    if field_elements is None:
        print('test')
        field_elements = elements
    new_label1 = ''
    new_label2 = ''
    new_label3 = ''
    for element in field_elements:
        if 'source' not in element['data']:
            new_label1 = element['data']['custom1']['field_name']
            new_label2 = element['data']['custom2']['field_name']
            new_label3 = element['data']['custom3']['field_name']

    print(new_label1)

    return new_label1, new_label2, new_label3, new_label1, new_label2, new_label3
