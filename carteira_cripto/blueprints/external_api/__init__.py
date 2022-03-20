from flask import Blueprint
from flask_restful import Api

from .resources import CoingeckoPrice

bp = Blueprint('external_api',\
                __name__,
                url_prefix='/api/v1')

api = Api(bp)
api.add_resource(CoingeckoPrice, '/price/<cryptos>/<currency>')

def init_app(app):
    app.register_blueprint(bp)