from dynaconf import settings
from flask_restful import Resource
import requests

class CoingeckoPrice(Resource):
    def get(self, cryptos, currency):
        url = settings.COINGECKO_API
        resp = requests.get(f'{url}simple/price?ids={cryptos}&vs_currencies={currency}')
        return resp.json()