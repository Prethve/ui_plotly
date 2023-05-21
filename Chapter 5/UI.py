from dash import Dash, html, dcc, Input, Output

app = Dash()

app.layout = html.Div([
    dcc.Input(id='input_name', value='Your Input', type='text'),
    html.Div(id='output_name', children='')
])

@app.callback(
    Output(component_id='output_name', component_property='children' ),
    Input(component_id='input_name', component_property='value')
)
def changing_output(input_name):
    return f'Text:{input_name}' # This returns the component property 'children' in Output.


if __name__ == '__main__':
    app.run_server(debug=True)