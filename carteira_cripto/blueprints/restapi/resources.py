from flask import abort, jsonify, request
from flask_restful import Resource
from carteira_cripto.ext.database.models import *


class WalletCalc(Resource):
    def post(self):
        name = request.form['name']
        return(name)

## Selects
class SelectCryptocurrency(Resource):
    def get(self):
        # cryptos = Cryptocurrency.query.all() or abort(204)
        # cryptos = Wallet.query.all() or abort(204)
        # cryptos = User.query.all() or abort(204)
        cryptos = CryptocurrencyWallet.query.all() or abort(204)
        return jsonify(
            {'Cryptocurrency': [crypto.to_dict() for crypto in cryptos]}
        )

class SelectWallet(Resource):
    def get(self):
        ...

class SelectUser(Resource):
    def get(self):
        ...

class SelectAllCryptocurrencyWallet(Resource):
    def get(self, id_wallet):
        cryptos_wallet = CryptocurrencyWallet.query.filter_by(id_wallet=id_wallet).all()
        return jsonify(
            {'Wallet Values': [crypto_wallet.to_dict() for crypto_wallet in cryptos_wallet]}
        )

## Inserts

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


## Updates
        
class UpdateCryptocurrency(Resource):
    def put(self, id_criptocurrency):
        new_nm_cryptocurrency = request.form['new_nm_cryptocurrency']
        new_cd_cryptocurrency = request.form['new_cd_cryptocurrency']

        Cryptocurrency.query.filter_by(id_cryptocurrency=id_criptocurrency)\
                            .update(dict(
                                nm_cryptocurrency = new_nm_cryptocurrency ,
                                cd_cryptocurrency = new_cd_cryptocurrency
                            ))
        db.session.commit()

class UpdateWallet(Resource):
    def put(self, id_user, id_wallet):
        new_nm_wallet = request.form['new_nm_wallet']

        Wallet.query.filter_by(id_user=id_user, id_wallet=id_wallet)\
                        .update(dict(
                            nm_wallet = new_nm_wallet
                        ))
        db.session.commit()

class UpdateUser(Resource):
    def put(self, id_user):
        new_nm_username = request.form['new_nm_username']
        new_cd_password = request.form['new_cd_password']

        User.query.filter_by(id_user=id_user)\
                        .update(dict(
                            nm_username = new_nm_username,
                            cd_password = new_cd_password
                        ))
        db.session.commit()

class UpdateCryptocurrencyWallet(Resource):
    def put(self, id_cryptocurrency_wallet, id_wallet, id_cryptocurrency):
        new_nr_current_amount = request.form['new_nr_current_amount']
        new_nr_rating = request.form['new_nr_rating']

        CryptocurrencyWallet.query.filter_by(
                                        id_cryptocurrency_wallet=id_cryptocurrency_wallet,
                                        id_wallet=id_wallet,
                                        id_cryptocurrency=id_cryptocurrency
                                    )\
                                    .update(dict(
                                        nr_current_amount = new_nr_current_amount,
                                        nr_rating = new_nr_rating
                                    ))
        db.session.commit()