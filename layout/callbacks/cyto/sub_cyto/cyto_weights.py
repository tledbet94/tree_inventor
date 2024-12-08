from dash import callback, ctx, no_update, Input, Output, State
import copy

from layout.callbacks.cyto.helper_functions.weight_helper import \
    get_system_info, auto_balance_system, proximity_to_100


@callback(
    [
        Output('weights-store', 'data'),
        Output('manual-input-feedback', 'children'),
        Output('system-weights-progress', 'value'),
        Output('system-weights-progress', 'style'),
        Output('system-weights-progress', 'label'),
    ],
    [
        Input('weights-input-button', 'n_clicks')
    ],
    [
        State('weights-input', 'value'),
        State('cytoscape', 'elements'),
        State('manual-button', 'className')

    ]
)
def adjust_weights(weights_enter_clicks, weights_input_value,
                   elements, manual_class):
    # best practice is to use a deepcopy of elements
    elements = copy.deepcopy(elements) if elements else []

    triggered_id = ctx.triggered_id if ctx.triggered_id else None

    # WIP - setting up feedback/screen text on manual mode
    manual_feedback_intro = 'Manual mode status: '
    manual_feedback = manual_feedback_intro
    # initially the progress value is blank
    progress_value = no_update
    progress_style = no_update
    progress_label = no_update

    try:
        for element in elements:
            if element['data']['last_clicked'] == 'True':
                if element['data']['weight'] is not None:
                    try:
                        element['data']['weight'] = float(weights_input_value)
                    except (ValueError, TypeError) as e:
                        pass
                    break
    except KeyError as e:
        pass
    except Exception as e:
        pass

    # Determine the mode
    mode = 'auto'
    if 'active' in manual_class:
        mode = 'manual'

    # Recalculate system weight
    if mode == 'manual':
        # Update progress bar
        _, _, system_elements, system_weight, message = get_system_info(elements)

        progress_value = proximity_to_100(system_weight)
        progress_label = ''
        if system_weight != 100:
            progress_style = {'display': 'block'}
        else:
            progress_style = {'display': 'none'}
        manual_feedback = manual_feedback_intro + '\n' + message
    elif mode == 'auto':
        # Adjust weights automatically
        elements = auto_balance_system(elements)[0]
        for element in elements:
            element['data']['invalid_weight'] = 'False'
        progress_value = 0
        progress_label = ''
        progress_style = {'display': 'none'}
        manual_feedback = ''

    # removed manual_input_feedback_children
    return elements, manual_feedback, progress_value, progress_style, progress_label
