from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

soccer_players = pd.read_csv('/Users/deevprethve/Documents/Coding/Plotly Dash/training_files/Python-Interactive-Dashboards-with-Plotly-Dash/fifa_soccer_players.csv')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard'),
    dbc.Row([
        dbc.Col(
                html.P(['Source: ',
                    html.A('Sofifa',
                            href= '',
                            target='_blank')
                        ])
                ),

        dbc.Col([
                html.Label('Player: '),
                dcc.Dropdown(options=soccer_players['long_name'].unique(),
                             value=soccer_players['long_name'].unique()[0],
                             id='player_select')
                ])
            ])
])

if __name__ == '__main__':
    app.run_server(debug=True)