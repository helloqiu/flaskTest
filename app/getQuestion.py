import sqlite3_db
import string


def get_question(kind, titleOnly=True, num='0'):
    if titleOnly:
        query = 'select title,score from question where kind = %s order by score desc' % kind
        cur = sqlite3_db.connect_db().execute(query)
        rv = cur.fetchall()
        cur.close()
        return rv
    else:
        query = 'select title,content,answer,kind,score from question where num = %d order by score desc' % string.atoi(
            num)
        cur = sqlite3_db.connect_db().execute(query)
        rv = cur.fetchall()
        cur.close()
        rv = rv[0]
        return rv
