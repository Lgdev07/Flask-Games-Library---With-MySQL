from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Jogo
from dao import JogoDao, UsuarioDao
import time
from jogoteca import db, app
from helpers import deleta_arquivo, recupera_imagem

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/lista')
def lista():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista, logado=session['usuario_logado'])

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    nome_imagem = recupera_imagem(id)
    return render_template('novo.html', titulo='Novo Jogo', capa_jogo=nome_imagem or "capa_padrao.jpg")

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    usuario_id = session['usuario_logado']
    jogo = Jogo(nome, categoria, console, usuario_id)
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    timestamp = time.time()
    arquivo.save(f'{app.config["UPLOAD_PATH"]}/capa{jogo.id}-{timestamp}.jpg')
    return redirect(url_for('lista'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    jogo = jogo_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Jogo', jogo=jogo, capa_jogo=nome_imagem or "capa_padrao.jpg")

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    usuario_id = session['usuario_logado']
    jogo = Jogo(nome, categoria, console, usuario_id, id = request.form['id'])
    jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(jogo.id)
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}')
    return redirect(url_for('lista'))

@app.route('/deletar/<int:id>')
def deletar(id):
    jogo_dao.deletar(id)
    flash('O Jogo foi removido com sucesso!')
    return redirect(url_for('lista'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(url_for('lista'))
        else:
            flash('Senha incorreta, tente denovo!')
            return redirect(url_for('login'))
    else:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

@app.route('/novo_usuario')
def novo_usuario():
    return render_template('novo_usuario.html', titulo='Criar Usuário')

@app.route('/cria_usuario', methods=['POST', ])
def cria_usuario():
    usuario_id = request.form['id']
    if len(usuario_id) > 8:
        flash('O id deve ter até 8 caracteres')
        return redirect(url_for('novo_usuario'))
    else:
        usuario_nome = request.form['nome']
        usuario_senha = request.form['senha']
        usuario_dao.cria_usuario(usuario_id, usuario_nome, usuario_senha)
        flash(f'Usuário {usuario_nome} criado com sucesso!')
        return redirect(url_for('login'))
