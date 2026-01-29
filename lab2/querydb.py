import sqlite3

conn = sqlite3.connect('test.db')
rows = conn.execute('''SELECT * FROM COMPANY;''')
for row in rows:
   print(row[0], row[1], row[2], row[3], row[4])
conn.close()