import sqlite3
conn = sqlite3.connect('mathop.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS addition(num1 int,num2 int,result TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS sub(num1 int,num2 int,result TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS mul(num1 int,num2 int,result TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS div(num1 int,num2 int,result TEXT)")
conn.commit()
cur.close()