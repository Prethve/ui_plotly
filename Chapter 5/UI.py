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
            dcc.RadioItems(id='radio_options',
                           options={
                               'happiness_rank':'Happiness Rank',
                               'happiness_score':'Happiness Score'
                           },
                           value='happiness_rank'),
            dcc.Graph(id='happiness_graph'),
            html.Div(id='happiness_mean', children='')
])

@app.callback(
    Output(component_id='happiness_graph', component_property='figure'),
    Output(component_id='happiness_mean', component_property='children'),
    Input(component_id='country_input',component_property='value'),
    Input(component_id='radio_options', component_property='value')
)
def update_graph(selected_country, selected_option):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    country_mean = filtered_happiness[selected_option].mean()
    line_fig = px.line(filtered_happiness,
                       x='year',
                       y=selected_option,
                       title=f'{selected_option} in {selected_country}')
    return line_fig, f'The {selected_option} of {selected_country} is {country_mean}'

if __name__ == '__main__':
    app.run_server(debug=True)