# app_instance.py
import dash
import dash_bootstrap_components as dbc
import gunicorn

from layout.layout import layout

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.MORPH,
        "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
    ]
)

server = app.server
app.layout = layout
