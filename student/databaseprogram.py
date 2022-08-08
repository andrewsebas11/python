import sqlite3
conn = sqlite3.connect('student.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS studentdetails(Id int, name text, m1 int, m2 int, m3 int, total int, average float)")
conn.commit()
cur.close()