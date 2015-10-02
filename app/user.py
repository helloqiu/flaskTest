import sqlite3_db
def register(username , password):
	query = 'select password from user where username = \'' + username + '\''
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	if not rv:
		query = 'insert into user values(\'' + username + '\',\'' + password + '\')';
		db = sqlite3_db.connect_db()
		db.execute(query)
		db.commit()
		return True
	else:
		return False

def rank():
	query='select username,score from user order by score desc'
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	return rv

def login(username , password):
	query = 'select password from user where username = \'' + username + '\''
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	if rv is None:
		return False
	else:
		if rv[0][0] == unicode(password):
			return True
		else:
			return False
