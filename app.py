import json
from flask import Flask, render_template, request
from conexao import Conexao
from datetime import datetime
from dateutil import parser

from models.extrato import Extrato

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
    conn = Conexao('Extrato', 'Data_Movimento')
    dados = conn.Get()
    
    _lista_extrato = []
    _saldo = 0
    _tipo_movimento = ''
    for d in dados:
        if d['Tipo_Movimento'] == 'C':
            _tipo_movimento = 'Entrada'
            _saldo = _saldo + float(d['Valor'])
        else:
            _tipo_movimento = 'Saída'
            _saldo = _saldo - float(d['Valor'])
    
        extrato = Extrato(d['Data_Movimento'], d['Valor'], _tipo_movimento, d['Categoria'], d['Descricao'], False, _saldo)    
        _lista_extrato.append(extrato)
    
    return render_template('extrato/index.html', extratos=_lista_extrato)


@app.route('/extrato/create', methods=['POST', 'GET'])
def extrato_create():
    if request.method == 'POST':
        conn = Conexao('Extrato', '')
        extrato = Extrato(request.form['Data_Movimento'], request.form['Valor'], request.form['Tipo_Movimento'], request.form['Categoria'], request.form['Descricao'], False)
        dados = conn.Post(data_to_send=extrato.ToJSON())
        
        return render_template('extrato/index.html')
    else:
        conn = Conexao('Categoria', 'Categoria')
        dados = conn.Get()
        return render_template('extrato/create.html', categorias=dados)

@app.template_filter('to_date')
def converto_to_date(value):
    return datetime.strftime(parser.parse(value), '%d/%m/%Y')

if __name__ == '__main__':
    app.run()