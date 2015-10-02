import sqlite3_db
def get_question(kind , titleOnly=True , num = '0'):
	if titleOnly:
		query='select title,score from question where kind = ' + kind + ' order by score desc'
		cur = sqlite3_db.connect_db().execute(query)
		rv = cur.fetchall()
		cur.close()
		return rv
	else:
		query='select title,content,answer,kind from question where num = ' + num + ' order by score desc'
		cur = sqlite3_db.connect_db().execute(query)
		rv = cur.fetchall()
		cur.close()
		rv = rv[0]
		return rv