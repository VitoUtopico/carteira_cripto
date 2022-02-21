from sqlalchemy import ForeignKey
from carteira_cripto.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Cryptocurrency(db.Model, SerializerMixin):
    __tablename__ = 'cryptocurrency'
    id_cryptocurrency = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nm_cryptocurrency = db.Column(db.String(140))
    cd_cryptocurrency = db.Column(db.String(10))

class CryptocurrencyWallet(db.Model, SerializerMixin):
    __tablename__ = 'cryptocurrency_wallet'
    id_cryptocurrency_wallet = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_wallet= db.Column(db.Integer)
    id_cryptocurrency = db.Column(db.Integer)
    nr_current_amount = db.Column(db.Numeric())
    nr_rating = db.Column(db.Integer)


class User(db.Model, SerializerMixin):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True)
    nm_username = db.Column(db.String(140))
    cd_password = db.Column(db.String(512))

class Wallet(db.Model, SerializerMixin):
    __tablename__ = 'wallet'
    id_wallet = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    nm_wallet = db.Column(db.String(140))
