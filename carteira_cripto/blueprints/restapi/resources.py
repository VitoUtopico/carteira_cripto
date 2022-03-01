from flask import abort, jsonify, request
from flask_restful import Resource
from carteira_cripto.ext.database.models import *


class WalletCalc(Resource):
    def post(self):
        name = request.form['name']
        return(name)

class ListCryptocurrency(Resource):
    def get(self):
        # cryptos = Cryptocurrency.query.all() or abort(204)
        # cryptos = Wallet.query.all() or abort(204)
        # cryptos = User.query.all() or abort(204)
        cryptos = CryptocurrencyWallet.query.all() or abort(204)
        print(cryptos)
        return jsonify(
            {'Cryptocurrency': [crypto.to_dict() for crypto in cryptos]}
        )

class InsertCryptocurrency(Resource):
    def post(self):
        data = [
                    Cryptocurrency(
                        nm_cryptocurrency = request.form['nm_cryptocurrency'],
                        cd_cryptocurrency = request.form['cd_cryptocurrency']
                    )
                ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        

class InsertWallet(Resource):
    def post(self):
        data = [
                    Wallet(
                        id_user = request.form['id_user'],
                        nm_wallet = request.form['nm_wallet']
                    )
                ]
        db.session.bulk_save_objects(data)
        db.session.commit()

class InsertUser(Resource):
    def post(self):
        data = [
                    User(
                        nm_username = request.form['nm_username'],
                        cd_password = request.form['cd_password']
                    )
                ]
        db.session.bulk_save_objects(data)
        db.session.commit()

class InsertCryptocurrencyWallet(Resource):
    def post(self):
        data = [
                    CryptocurrencyWallet(
                        id_wallet= request.form['id_wallet'],
                        id_cryptocurrency = request.form['id_cryptocurrency'],
                        nr_current_amount = request.form['nr_current_amount'],
                        nr_rating = request.form['nr_rating']
                    )
                ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        