from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

avocado = pd.read_csv('/Users/deevprethve/Documents/Coding/Plotly Dash/training_files/Python-Interactive-Dashboards-with-Plotly-Dash/avocado.csv')

app.layout = html.Div([
    html.Div('Avocado Prices Dashboard'),
    html.Br(),
    dcc.Dropdown(id='region_select',
                 options=avocado['geography'].unique(),
                 value='New York'),
    dcc.Graph(id='avocado_graph')
])

@app.callback(
    Output(component_id='avocado_graph', component_property='figure'),
    Input(component_id='region_select', component_property='value')
)
def avocado_line(selected_region):
    filtered_region = avocado[avocado['geography'] == selected_region]
    line_px = px.line(filtered_region,
                      x='date',
                      y='average_price',
                      color='type',
                      title=f'Avocado prices in {selected_region}')
    return line_px


if __name__ == '__main__':
    app.run_server(debug=True)