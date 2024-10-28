# app.py
from app_instance import app
from layout.layout import layout
from callbacks.panels.info import info_callback

app.layout = layout

if __name__ == '__main__':
    app.run(debug=True, port='8051')
