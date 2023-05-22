from dash import Dash, html, dcc, Input, Output, State
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
            dcc.RadioItems(id='region_select',
                           options=happiness['region'].unique(),
                           value='North America'),
            dcc.Dropdown(options=(happiness['country']).unique(), 
                         value='United States', 
                         id='country_input'),
            dcc.RadioItems(id='radio_options',
                           options={
                               'happiness_rank':'Happiness Rank',
                               'happiness_score':'Happiness Score'
                           },
                           value='happiness_rank'),
            html.Br(),
            html.Button(id='update_button',
                        n_clicks=0,
                        children='Update output'),
            dcc.Graph(id='happiness_graph'),
            html.Div(id='happiness_mean', children='')
])

@app.callback(
        Output(component_id='country_input', component_property='options'),
        Output(component_id='country_input', component_property='value'),
        Input(component_id='region_select', component_property='value')
)
def region_update(region_input):
    filtered_happiness = happiness[happiness['region'] == region_input]
    country_options = filtered_happiness['country'].unique()

    return country_options, country_options[0]


@app.callback(
    Output(component_id='happiness_graph', component_property='figure'),
    Output(component_id='happiness_mean', component_property='children'),
    Input(component_id='update_button', component_property='n_clicks'),
    State(component_id='country_input',component_property='value'),
    State(component_id='radio_options', component_property='value')
)
def update_graph(button_click, selected_country, selected_option):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    country_mean = filtered_happiness[selected_option].mean()
    line_fig = px.line(filtered_happiness,
                       x='year',
                       y=selected_option,
                       title=f'{selected_option} in {selected_country}')
    return line_fig, f'The {selected_option} of {selected_country} is {country_mean}'

if __name__ == '__main__':
    app.run_server(debug=True)