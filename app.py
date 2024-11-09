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

app.layout = layout

if __name__ == '__main__':
    app.run(debug=True, port='8051')
