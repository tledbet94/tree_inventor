from dash import Input, Output, State
from app_instance import app


@app.callback(
    Output("book-modal", "is_open"),
    [Input("book-button", "n_clicks"),
     Input("modal-close-button", "n_clicks")],
    [State("book-modal", "is_open")],
)
def toggle_book_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open