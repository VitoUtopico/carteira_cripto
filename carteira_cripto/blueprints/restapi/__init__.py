from flask import Blueprint
from flask_restful import Api

from .resources import WalletCalc,\
                        SelectAllCryptocurrency,\
                        SelectCryptocurrencyWalletById,\
                        SelectCryptocurrencyById,\
                        InsertCryptocurrency,\
                        InsertWallet,\
                        InsertUser,\
                        InsertCryptocurrencyWallet,\
                        UpdateCryptocurrency,\
                        UpdateWallet,\
                        UpdateUser,\
                        UpdateCryptocurrencyWallet

bp = Blueprint('restapi',\
                __name__,
                url_prefix='/api/v1')
api = Api(bp)
api.add_resource(WalletCalc, '/calcs/')
api.add_resource(SelectAllCryptocurrency, '/cryptos/')
api.add_resource(SelectCryptocurrencyById, '/cryptos/<id_cryptocurrency>')
api.add_resource(SelectCryptocurrencyWalletById, '/crypto_wallet/<id_wallet>/')

api.add_resource(InsertCryptocurrency, '/insertcrypto/')
api.add_resource(InsertWallet, '/insertwallet/')
api.add_resource(InsertUser, '/insertuser/')
api.add_resource(InsertCryptocurrencyWallet, '/insertcryptowallet/')

api.add_resource(UpdateCryptocurrency, '/updatecrypto/<id_criptocurrency>')
api.add_resource(UpdateWallet, '/updatewallet/<id_user>/<id_wallet>')
api.add_resource(UpdateUser, '/updateuser/<id_user>')
api.add_resource(UpdateCryptocurrencyWallet, '/updatecryptowallet/<id_cryptocurrency_wallet>/<id_wallet>/<id_cryptocurrency>')


def init_app(app):
    app.register_blueprint(bp)