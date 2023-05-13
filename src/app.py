from dash import Dash, html, dcc

app = Dash(__name__)
server = app.server #server heroku/render reconhecer a app

app.layout = html.Div(children=[
    html.H1(children='Meu primeiro projeto', className='banner'),
        html.Br(),
        html.Div(children=[
            html.A('Exemplo 1:')
            ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)