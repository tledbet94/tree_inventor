# app.py
from app_instance import app

# Internal imports
from layout.layout import layout

# Internal callbacks
from layout.callbacks.bottom_row.bottom_row_callback import update_active_button
from layout.callbacks.controls.panel_change import update_mode
from layout.callbacks.controls.home.book_button import toggle_book_modal
from layout.callbacks.controls.edit.edit_button_highlight import manage_edit_button_highlight
from layout.callbacks.controls.edit.edit_input import show_edit_input, edit_check_input
from layout.callbacks.info import info_callback
from layout.callbacks.cyto.cyto_callback import modify_cyto
from layout.callbacks.controls.algo.slider import display_value
from layout.callbacks.controls.algo.traversal_deactivate import update_disabled_buttons
from layout.callbacks.controls.weights.weights_input_callback import show_weights_input
from layout.callbacks.controls.weights.manual_active_pressed import update_manual_auto_buttons
from layout.callbacks.controls.custom_fields.active_button_callback import update_fields_buttons
from layout.callbacks.controls.custom_fields.view_switch import change_fields_view


app.layout = layout

if __name__ == '__main__':
    app.run(debug=True, port='8051')
