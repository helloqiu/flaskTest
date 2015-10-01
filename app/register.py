import sqlite3_db
def register(username , password):
	query = 'select password from user where username = \'' + username + '\''
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	if not rv:
		#regist
		return True
	else:
		return False
