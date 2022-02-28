from flask import abort, jsonify, request
from flask_restful import Resource
from carteira_cripto.ext.database.models import *


class WalletCalc(Resource):
    def post(self):
        name = request.form['name']
        return(name)

class ReadCryptocurrency(Resource):
    def get(self):
        cryptos = Cryptocurrency.query.all() or abort(204)
        print(cryptos)
        return jsonify(
            {'Cryptocurrency': [crypto.to_dict() for crypto in cryptos]}
        )