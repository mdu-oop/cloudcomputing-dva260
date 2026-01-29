import sqlite3
import sys
import random

n = sys.argv[1]
a = random.randint(20, 60)
s = round(random.uniform(20000, 60000), 2)

conn = sqlite3.connect('test.db')
conn.execute(f'''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   VALUES (1, "{n}", {a}, "Wallingatan 32, 11124 Stockholm", {s});''')
conn.commit()
conn.close()