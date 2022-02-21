from importlib import resources
from attr import validate
from flask import Blueprint
from flask_restful import Api

from .resources import WalletCalc

bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)
api.add_resource(WalletCalc, '/calcs/')


def init_app(app):
    app.register_blueprint(bp)