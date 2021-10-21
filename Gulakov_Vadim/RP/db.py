import sqlite3 as sql

con = sql.connect("News.db")

def create_db():
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS News(
                      ID INTEGER PRIMARY KEY, 
                      Pubdata DATE,
                      Link TEXT,
                      Text TEXT,
                      Image TEXT
                      )
                      ''')
        con.commit()
        cur.close()


