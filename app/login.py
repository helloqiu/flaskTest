import sqlite3
from flask import g

DATABASE = './db/dataBase.sqlite3'

def get_db():
	db = getattr(g , '_database' , None)
	if db is None:
		db = g._database = connect_to_database()
	return db


def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def login(username , password):
	query = 'select password from user where username = ?'
	cur = get_db().execute(query , username)
	rv = cur.fetchall()
	cur.close()
	rv = rv[0] if rv else None
	if rv is None:
		return False
	else:
		if rv == password:
			return True
		else:
			return False
