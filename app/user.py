import sqlite3_db
def register(username , password):
	query = 'select password from user where username = \'%s\'' %username
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	if not rv:
		#query = 'insert into user values(\'' + username + '\',\'' + password + '\', 0,0)';
		query = 'insert into user values(\'%s\' , \'%s\' , 0,0)' %(username , password)
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
	query = 'select password from user where username = \'%s\'' %username
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
def add_score(username , score):
	query1 = 'select score from user where username =\'%s\'' %username
	cur = sqlite3_db.connect_db().execute(query1)
	rv = cur.fetchall()
	cur.close()
	nowScore = rv[0][0]
	query = 'update user set score = ' + '%d' %(nowScore + score) + ' where username = \'' + username + '\''
	query = 'update user set score = %d where username = \'%s\'' %(nowScore + score , username)
	db = sqlite3_db.connect_db()
	db.execute(query)
	db.commit()

