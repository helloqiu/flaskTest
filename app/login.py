import sqlite3_db
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
