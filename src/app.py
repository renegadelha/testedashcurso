from dash import Dash, html, dcc,dash_table, State, exceptions
from dash.dependencies import Input, Output

app = Dash(__name__)
server = app.server #server heroku/render reconhecer a app

#app.server.config['SQLALCHEMY_DATABASE_UTI'] =  'postgres://renegadelha:slPivjRyiDdTsJcnKiP5LNMBLLHhHNcc@dpg-chfq67bhp8u065r7hqi0-a.oregon-postgres.render.com/dbacesso'

usuarios =  [{'id': 1, 'login': 'rene','nome':'rene de sousa'}, {'id': 2, 'login': 'ze','nome':'jose da silva'}]
senhas = {'rene':'rene', 'ze':'pass2'}
produtos = {'rene':[],'ze':[]}

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
    ,
    html.Br(),
    html.Div(children=[
            html.H3('Login')
        ]),
        html.Div(['Login:',
                dcc.Input(id='loginValid',  type='text'),
                ])
                ,
        html.Div(['Senha:',
                dcc.Input(id='senhaValid',type='password'),
                html.Button(id='fazerLogin', n_clicks=0, children='Logar')
                ])
        ,

        html.Div(id='menuLogado',
                         children=[]
                         )
])

@app.callback(
    Output('menuLogado', 'children'),
    Input('fazerLogin', 'n_clicks'),
    State('loginValid', 'value'),
    State('senhaValid', 'value'),
    prevent_initial_call=True

)
def logar(n_clicks, login, senha):
    global usuarios
    global senhas

    if login == None or senha == None:
        raise exceptions.PreventUpdate

    elif not login == None and not senha == None:

        sucesso = False
        for user in usuarios:
            if user['login'] == login:
                if senhas[login] == senha:
                    sucesso = True

        if sucesso:
            return html.Div(children=[
                html.Br(),
                html.P(children='1-Cadastrar Produto'),
                html.P(children='1-Cadastrar Produto'),
                html.P(children='1-Cadastrar Produto'),
                html.P(children='1-Cadastrar Produto'),
                html.P(children='1-Cadastrar Produto'),

            ])
        else:
            return html.Div(children=[
                html.A(style={'color':'red'}, children='Usuário ou Senha incorreta')
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
    global produtos

    if len(inputNomeCompleto) > 0 and len(inputLogin) > 0 and len(inputSenha) > 0:
        if len(usuarios) == 0:
            id = 0
        else:
            id = int(usuarios[-1]['id']) + 1

        usuarios.append({'id': id, 'login': inputLogin,'nome':inputNomeCompleto})
        senhas[inputLogin] = inputSenha
        produtos[inputLogin] = []

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