from dash import ctx, no_update, Input, Output, State
from app_instance import app
import copy

from layout.callbacks.cyto.helper_functions.weight_helper import \
    get_system_info, auto_balance_system, proximity_to_100


@app.callback(
    Output('weights-store', 'data'),
    Output('manual-input-feedback', 'children'),
    Output('system-weights-progress', 'value'),
    Output('system-weights-progress', 'style'),
    Output('system-weights-progress', 'label'),
    [
        Input('weights-input-button', 'n_clicks'),
    ],
    [
        State('cytoscape', 'elements'),
        State('weights-input', 'value'),
        State('manual-button', 'className'),
        State('auto-button', 'className'),
        State('cytoscape', 'tapNode'),
        State('cytoscape', 'tapEdge'),
    ]
)
def adjust_weights(weights_enter_clicks,
                   elements, weights_input_value, manual_button_classname, auto_button_classname,
                   tap_node, tap_edge):
    elements = copy.deepcopy(elements) if elements else []
    manual_input_feedback = no_update
    progress_value = no_update
    progress_style = no_update
    progress_label = no_update

    # Determine the mode
    if 'active' in manual_button_classname:
        mode = 'manual'
    elif 'active' in auto_button_classname:
        mode = 'automatic'
    else:
        mode = 'manual'  # Default to manual

    # Convert input value to float
    try:
        entered_weight = float(weights_input_value)
    except (ValueError, TypeError):
        entered_weight = 0.0

    entered_weight = max(0.0, min(entered_weight, 100.0))

    selected_element = None
    for element in elements:
        if element['data']['last_clicked'] == 'True':
            element['data']['weight'] = entered_weight
            selected_element = element
            break

    if not selected_element:
        manual_input_feedback = "No element selected. Please select a node or edge."
        # removed manual_input_feedback
        return elements, manual_input_feedback, progress_value, progress_style, progress_label

    # Recalculate system weight
    _, _, system_elements, system_weight, message = get_system_info(elements)

    if mode == 'manual':
        # Update progress bar
        progress_value = proximity_to_100(system_weight)
        progress_label = ''
        if system_weight != 100:
            progress_style = {'display': 'block'}
        else:
            progress_style = {'display': 'none'}
        manual_input_feedback = message
    elif mode == 'automatic':
        # Adjust weights automatically
        elements, feedback_message = auto_balance_system(elements)
        selected_element, element_type, system_elements, system_weight, feedback_message = get_system_info(elements)
        progress_value = 0
        progress_label = ''
        progress_style = {'display': 'none'}
        manual_input_feedback = feedback_message

    # removed manual_input_feedback_children
    return elements, manual_input_feedback, progress_value, progress_style, progress_label
