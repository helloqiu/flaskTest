import sqlite3_db
def rank():
	query='select username,score from user order by score desc'
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	return rv