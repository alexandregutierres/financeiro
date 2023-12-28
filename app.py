from flask import Flask, render_template, redirect
import pandas as pd
import requests
import plotly.express as px
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')   

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/categorias')
def categorias():
    api_url = 'https://parseapi.back4app.com/classes/Categoria'
 
    headers  = {"accept": "application/json",
                "X-Parse-Application-Id" : "5qYGdcl6opRF8nltPYjOOIFCatF40inhOyXYLpdo",
                "X-Parse-REST-API-Key" : "oE6cpdY1BEuP8m0UED9fsMoSkGDfy3ATWbrOU9sR"}
    

    response = requests.get(api_url, headers=headers)
    dados = response.json()['results']
    
    return render_template('categorias/index.html', categorias=dados)



@app.route('/categorias/create')
def categoria_create():
    return render_template('categorias/create.html')


if __name__ == '__main__':
    app.run()