from flask_sqlalchemy import SQLAlchemy 
from .models import Scrap

def add_scrap_to_db(dictionnaire,url):
    db = SQLAlchemy()
    new_scrap= Scrap(text=dictionnaire,url=url)
    db.session.add(new_scrap)
    db.session.commit()
    id=new_scrap.id
    return id

def delete_scrap_from_db(id_to_delete):
    db = SQLAlchemy()
    u = db.session.get(Scrap, id_to_delete)
    db.session.delete(u)
    db.session.commit()
    return print("Delete sucessful!")

def show_scrap(id_to_show):
    db = SQLAlchemy()
    u = db.session.get(Scrap, id_to_show)
    return u.text, u.url

def show_all_scrap():
    db = SQLAlchemy()
    u = Scrap.query.all()
    return u

def delete_all_scrap():
    db = SQLAlchemy()
    db.session.query(Scrap).delete()
    db.session.commit() 
    return ("DB deleted!")