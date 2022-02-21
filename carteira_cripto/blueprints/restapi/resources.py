from flask import abort, jsonify, request
from flask_restful import Resource
from carteira_cripto.ext.database.models import *

class WalletCalc(Resource):
    def post(self):
        name = request.form['name']
        return(name)
