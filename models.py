import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = os.environ['DATABASE_URL']


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#Create Movie table in db-------------------------------------/
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    releasedate = db.Column(db.DateTime())

    def __init__(self, title, releasedate):
        self.title = title
        self.releasedate = releasedate
       
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'releasedate': self.releasedate
        }

#Create Actor table in db-------------------------------------/
class Actor(db.Model):
    __tablename__ = 'actors' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    movieid = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    
    def __init__(self, name, age, gender, movieid):
        self.name = name
        self.age = age
        self.gender = gender
        self.movieid = movieid
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'gender': self.gender,
        'movieid': self.movieid,
        }
#----------------------------------------------\
