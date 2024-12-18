import time
import gunicorn
import dash
import dash_bootstrap_components as dbc

# Internal imports
from layout.layout import layout

# Internal callbacks
from layout.callbacks.bottom_row.bottom_row_callback import update_active_button
from layout.callbacks.controls.panel_change import update_mode

from layout.callbacks.controls.home.book_button import toggle_book_modal
from layout.callbacks.controls.home.card import update_card

from layout.callbacks.controls.edit.edit_button_highlight import manage_edit_button_highlight
from layout.callbacks.controls.edit.edit_input import show_edit_input, edit_check_input

from layout.callbacks.info import info_callback

from layout.callbacks.controls.algo.slider import display_value
from layout.callbacks.controls.algo.traversal_deactivate import update_disabled_buttons

from layout.callbacks.controls.weights.weights_input_callback import show_weights_input
from layout.callbacks.controls.weights.manual_active_pressed import update_manual_auto_buttons
from layout.callbacks.controls.weights.main_screen_callback import update_main_screen

from layout.callbacks.controls.custom_fields.active_button_callback import update_fields_buttons
from layout.callbacks.controls.custom_fields.input_management import manage_inputs

from layout.callbacks.cyto.sub_cyto.cyto_fields import fields_update
from layout.callbacks.cyto.sub_cyto.cyto_edit import modify_elements
from layout.callbacks.cyto.sub_cyto.cyto_traversal import handle_traversals
from layout.callbacks.cyto.sub_cyto.cyto_weights import adjust_weights

from layout.callbacks.cyto.main_cyto import update_cytoscape_elements

from layout.callbacks.controls.templates.active_button import update_active_template_button
from layout.callbacks.cyto.sub_cyto.cyto_template import swap_trees

from layout.callbacks.controls.save_load.local_save import local_save
from layout.callbacks.controls.file_info import update_file_info
from layout.callbacks.controls.save_load.local_upload import upload_tree

from layout.callbacks.controls.themes.active_theme_button import update_buttons
from layout.callbacks.controls.themes.theme_update import theme_update

from layout.callbacks.cyto.switch_view import change_cyto_view

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.MORPH,
        "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
    ],
)

server = app.server
app.layout = layout

if __name__ == '__main__':
    # Add a 3-second delay before starting the server
    time.sleep(1)
    app.run(debug=True, port='8054')
