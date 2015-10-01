import sqlite3_db
def login(username , password):
	query = 'select password from user where username = \'' + username + '\''
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	rv = rv[0] if rv else None
	if rv is None:
		return False
	else:
		if rv[0] == unicode(password):
			return True
		else:
			return False
