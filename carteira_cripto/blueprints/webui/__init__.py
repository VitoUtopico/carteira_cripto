from flask import Blueprint

from .views import index , price

bp = Blueprint('webui', __name__, template_folder='templates')

bp.add_url_rule('/', view_func=index)
bp.add_url_rule('/price/<criptos>/<currency>', view_func=price)


def init_app(app):
    app.register_blueprint(bp)