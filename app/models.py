from . import db
from sqlalchemy.sql import func


class Scrap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    url= db.Column(db.String(10000))

