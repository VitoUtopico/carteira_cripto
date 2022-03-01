from importlib import resources
from mimetypes import init
from attr import validate
from flask import Blueprint
from flask_restful import Api

from .resources import WalletCalc,\
                        ListCryptocurrency,\
                        InsertCryptocurrency,\
                        InsertWallet,\
                        InsertUser,\
                        InsertCryptocurrencyWallet

bp = Blueprint('restapi',\
                __name__,
                url_prefix='/api/v1')
api = Api(bp)
api.add_resource(WalletCalc, '/calcs/')
api.add_resource(ListCryptocurrency, '/cryptos/')
api.add_resource(InsertCryptocurrency, '/insertcrypto/')
api.add_resource(InsertWallet, '/insertwallet/')
api.add_resource(InsertUser, '/insertuser/')
api.add_resource(InsertCryptocurrencyWallet, '/insertcryptowallet/')


def init_app(app):
    app.register_blueprint(bp)