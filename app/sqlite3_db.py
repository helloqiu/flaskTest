import sqlite3
from flask import g
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
import os
DATABASE = 'app/dataBase.sqlite3'
#basedir = os.path.abspath(os.path.dirname(__file__))
#db = SQLAlchemy(app)


'''class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(64), unique=True,
                         primary_key=True, index=True)
    password = db.Column(db.String)
    score = db.Column(db.Integer, default=0)
    achievement = db.Column(db.Unicode)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, unique=True, primary_key=True, index=True)
    title = db.Column(db.Unicode)
    content = db.Column(db.UnicodeText)
    score = db.Column(db.Integer)
    answer = db.Column(db.Unicode)
    kind = db.Column(db.Integer)
'''
def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

