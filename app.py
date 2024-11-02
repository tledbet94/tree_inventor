# app.py
from app_instance import app
from layout.layout import layout

# Internal callbacks
from layout.callbacks.bottom_row.bottom_row_callback import update_active_button
from layout.callbacks.controls import book_button
from layout.callbacks.controls.panel_change import update_mode
from layout.callbacks.info import info_callback

app.layout = layout

if __name__ == '__main__':
    app.run(debug=True, port='8051')
