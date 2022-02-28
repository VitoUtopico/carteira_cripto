from carteira_cripto.ext.database import db
from carteira_cripto.ext.database.models import *


def createdb():
    '''Creates database'''
    db.create_all()

def dropdb():
    """Cleans database"""
    db.drop_all()

def populatedb():
    data = [
        Cryptocurrency(
            id_cryptocurrency = 1,
            nm_cryptocurrency = 'bitcoin',
            cd_cryptocurrency = 'btc'
        ),
        Cryptocurrency(
            id_cryptocurrency = 2,
            nm_cryptocurrency = 'cardano',
            cd_cryptocurrency = 'ada'
        ),
        CryptocurrencyWallet(
            id_cryptocurrency_wallet = 1,
            id_wallet= 1,
            id_cryptocurrency = 1,
            nr_current_amount = 0.028,
            nr_rating = 100,
        ),
        CryptocurrencyWallet(
            id_cryptocurrency_wallet = 2,
            id_wallet= 1,
            id_cryptocurrency = 2,
            nr_current_amount = 5.237,
            nr_rating = 90,
        ),
        User(
            id_user = 1,
            nm_username = 'Test User',
            cd_password = 'Test_User.1234'
        ),
        Wallet(
            id_wallet = 1,
            id_user = 1,
            nm_wallet = 'Carteira Teste'
        )
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    