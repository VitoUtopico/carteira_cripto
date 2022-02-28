from importlib import resources
from mimetypes import init
from attr import validate
from flask import Blueprint
from flask_restful import Api

from .resources import WalletCalc, ReadCryptocurrency

bp = Blueprint('restapi',\
                __name__,
                url_prefix='/api/v1')
api = Api(bp)
api.add_resource(WalletCalc, '/calcs/')
api.add_resource(ReadCryptocurrency, '/criptos/')


def init_app(app):
    app.register_blueprint(bp)