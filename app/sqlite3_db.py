import sqlite3
from flask import g
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
import os
DATABASE = 'app/dataBase.sqlite3'
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    score = db.Column(db.Integer, default=0)
    achievement = db.Column(db.String)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return 'User %r' % self.username


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, unique=True, primary_key=True, index=True)
    title = db.Column(db.String)
    content = db.Column(db.UnicodeText)
    score = db.Column(db.Integer)
    answer = db.Column(db.String)
    kind = db.Column(db.Integer)

    def __repr__(self):
        return 'User %r' % self.title
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
'''
