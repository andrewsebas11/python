import pandas as pd
import sqlite3
conn = sqlite3.connect(r'C:\sqlite3\pandasexample.db')
sql = "select * from student"
ta = pd.read_sql(sql, conn)
df = pd.DataFrame(ta)
print(df)
print(df.shape)
print('----------------------------')
print(df.head(2))
print('----------------------------')
print(df.tail(2))
print('----------------------------')
print(df.describe())
print('-----------------------------')
print(df[-1:])
print('-----------------------------')
df['total'] = df['m1'] + df['m2'] + df['m3'] + df['m4'] + df['m5']
print(df)
print('-----------------------------')
df['average'] = (df['total']) / 5
print(df)
