from dash import Dash, html, dcc,dash_table, State, exceptions
from dash.dependencies import Input, Output

app = Dash(__name__)
server = app.server #server heroku/render reconhecer a app

#app.server.config['SQLALCHEMY_DATABASE_UTI'] =  'postgres://renegadelha:slPivjRyiDdTsJcnKiP5LNMBLLHhHNcc@dpg-chfq67bhp8u065r7hqi0-a.oregon-postgres.render.com/dbacesso'

usuarios =  [{'id': 1, 'login': 'rene','nome':'rene de sousa'}, {'id': 2, 'login': 'ze','nome':'jose da silva'}]
senhas = {'rene':'pass1', 'ze':'pass2'}

app.layout = html.Div(children=[
    html.H1(children='Meu primeiro projeto', className='banner'),
    html.Br(),
    html.Div(children=[
        html.H3('Adicionar Usuario')
    ]),
    html.Div(['Nome Completo:',
            dcc.Input(id='inputNomeCompleto',  type='text'),
            ])
            ,
    html.Div(['Login:',
            dcc.Input(id='inputLogin',type='text'),
            ])
    ,
    html.Div(['Senha:',
            dcc.Input(id='inputSenha',  type='password'),
            html.Button(id='botaoAddUsuario', n_clicks=0, children='Inserir Usuario')
            ])
    ,
    html.Div(id='users_output',
                     children=html.Div([
                                        dash_table.DataTable(
                                            id='table',
                                            data=usuarios
                                        )
                                        ])
                     )

])

@app.callback(
    Output('users_output', 'children'),
    Input('botaoAddUsuario', 'n_clicks'),
    State('inputNomeCompleto', 'value'),
    State('inputLogin', 'value'),
    State('inputSenha', 'value'),
    prevent_initial_call=True

)
def update_table(n_clicks, inputNomeCompleto, inputLogin, inputSenha):
    global usuarios
    global senhas

    if len(inputNomeCompleto) > 0 and len(inputLogin) > 0 and len(inputSenha) > 0:
        print(inputNomeCompleto)
        print(inputLogin)
        print(inputSenha)

        if len(usuarios) == 0:
            id = 0
        else:
            id = int(usuarios[-1]['id']) + 1

        usuarios.append({'id': id, 'login': inputLogin,'nome':inputNomeCompleto})
        senhas[inputLogin] = inputSenha

        child = html.Div([
            dash_table.DataTable(
                id='table',
                data = usuarios
            )
        ])

        return child

    elif len(inputNomeCompleto) == 0:
        raise exceptions.PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)