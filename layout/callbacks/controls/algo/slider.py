from dash import callback, Input, Output

def transform_value(value):
    return 10 ** value

@callback(Output('algo-slider-text', 'children'),
              Input('algo-slider', 'value'))
def display_value(value):
    return f"{10 ** value:,}" + " TRAVERSALS"