from flask import abort, render_template, jsonify
from dynaconf import settings
import requests

import ast

def index():
    return render_template('index.html')

def price(criptos, currency):
    url = settings.COINGECKO_API
    req = requests.get(f'{url}simple/price?ids={criptos}&vs_currencies={currency}').content.decode('utf-8')
    teste = ast.literal_eval(req)
    return render_template('prices.html', req=teste)