import dash
from dash import dcc, html 

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1('Poverty and Equity Database', style = {'color' : 'blue', 'fontSize': '40px'}),
    html.H2('The World Bank'),
    html.P('Key Facts:'),
    html.Ul([
        html.Li('Number of Economies: 1970'),
        html.Li('Temporal Coverage: 1974-2019'),
        html.Li('Update Frequency: Quarterly'),
        html.Li('Last Update: April 25, 2022'),
        html.Li([
            'Source: ',
            html.A('link', href='#')
        ])
    ])

])

if __name__ == ('__main__'):
    app.run_server(debug = True)
