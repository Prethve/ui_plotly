from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

happiness = pd.read_csv('/Users/deevprethve/Documents/Coding/Plotly Dash/training_files/Python-Interactive-Dashboards-with-Plotly-Dash/world_happiness.csv')


app.layout = html.Div([
    html.Div('World Happiness Dashboard'),
    html.P(['This dashboard shows the Happiness score.',
            html.Br(),
            html.A('World Happiness Report',
                   href='https://worldhappiness.report/ed/2023/',
                   target='_blank')]),
            dcc.Dropdown(options=(happiness['country']).unique(), 
                         value='United States', 
                         id='country_input'),
            dcc.Graph(id='happiness_graph')
])

@app.callback(
    Output(component_id='happiness_graph', component_property='figure'),
    Input(component_id='country_input',component_property='value'),
)
def update_graph(selected_country):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(filtered_happiness,
                       x='year',
                       y='happiness_score',
                       title=f'Happiness Score in {selected_country}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)