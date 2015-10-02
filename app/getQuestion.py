import sqlite3_db
def get_question(kind):
	query='select title,score from question where kind = ' + kind + ' order by score desc'
	cur = sqlite3_db.connect_db().execute(query)
	rv = cur.fetchall()
	cur.close()
	return rv