import sqlite3
conn = sqlite3.connect('task2.db')
conn.execute('''CREATE TABLE TASK2
 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
  TEMPERATURE INT NOT NULL,
  DATE TEXT  NOT NULL);''')
conn.close()