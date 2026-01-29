import sqlite3
from flask import g
from flask import Flask, request
from datetime import datetime


DATABASE = 'test.db'

def get_db():
   db = getattr(g,'_database', None)
   if db is None:
     db = g._database = sqlite3.connect(DATABASE)
   return db

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
   db = getattr(g,'_database', None)
   if db is not None:
      db.close()

@app.route('/store')
def store_data():
   data = request.args.get('data', default=0, type=int)

   conn = sqlite3.connect('task2.db')
   conn.execute(f'''INSERT INTO TASK2 (TEMPERATURE,DATE)
      VALUES ("{data}", datetime('now'));''')
   conn.commit()
   conn.close()

   result = "Temperate " + data + " stored: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   return result

@app.route('/show_data')
def show_data():
    result = ""
    conn = sqlite3.connect('task2.db')
    for row in conn.execute('''SELECT TEMPERATURE, DATE FROM TASK2'''):
        result += str(row[0]) + "°C on " + str(row[1]) + "<br>"
    return result

@app.route('/show_stats')
def show_stats():
    conn = sqlite3.connect('task2.db')
    rows = conn.execute('''SELECT  MIN(TEMPERATURE), MAX(TEMPERATURE), AVG(TEMPERATURE) FROM TASK2''')
    for row in rows:
        avg_temp = round(row[2], 2)
        min_temp = row[0]
        max_temp = row[1]
    result = f"min = {min_temp}°C<br>max = {max_temp}°C<br>avg = {avg_temp}°C"
    return result


if __name__ =='__main__':
   app.run(host='0.0.0.0', port=8080)

