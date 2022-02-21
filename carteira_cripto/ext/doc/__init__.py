from flask_pydantic_spec import FlaskPydanticSpec

spec = FlaskPydanticSpec('flask', title='Carteira Cripto')

def init_app(app):
    spec.register(app)