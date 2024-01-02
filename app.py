from flask import Flask, render_template, redirect
from conexao import Conexao

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')   

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/categorias')
def categorias():
    conn = Conexao('Categoria', 'Categoria')
    dados = conn.Get()
    
    return render_template('categorias/index.html', categorias=dados)

@app.route('/categorias/create')
def categoria_create():
    return render_template('categorias/create.html')

@app.route('/fluxocaixa')
def fluxocaixa():
    return render_template('fluxocaixa/index.html')

@app.route('/extrato')
def extrato():
    return render_template('extrato/index.html')


@app.route('/extrato/create')
def extrato_create():
    conn = Conexao('Categoria', 'Categoria')
    dados = conn.Get()
    
    return render_template('extrato/create.html', categorias=dados)


if __name__ == '__main__':
    app.run()