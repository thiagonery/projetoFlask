# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Mensagem


@app.route('/')
def index():
    mensagens = Mensagem.recupera_todas()

    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/mensagem',
                'texto': 'Escrever mensagem'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'mensagens': mensagens}

    return render_template('index.html', **context)

@app.route('/mensagem')
def mensagem():
    menu = []
    menu.append({'active': False,
                'href': '/',
                'texto': 'Página principal'})
    menu.append({'active': True,
                'href': '/mensagem',
                'texto': 'Escrever mensagem'})
    context = {'titulo': 'Escrever mensagem',
            'menu': menu}
    return render_template('mensagem.html', **context)


@app.route('/mensagem/gravar', methods=['POST'])
def gravar_mensagem():
    mensagem = Mensagem(request.form['usuario'], request.form['texto'])
    mensagem.gravar()
    return redirect('/')


app.run()
