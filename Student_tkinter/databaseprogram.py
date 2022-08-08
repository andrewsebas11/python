import sqlite3
conn = sqlite3.connect('std.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pass1(Id int, name text, m1 int, m2 int, m3 int)")
cur.execute("CREATE TABLE IF NOT EXISTS fail1(Id int, name text, m1 int, m2 int, m3 int)")
conn.commit()
cur.close()