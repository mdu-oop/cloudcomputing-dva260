

import sqlite3
from flask import g
from flask import Flask

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

@app.route('/show_data')
def show_data():
   rows = get_db().execute('''SELECT NAME,AGE FROM COMPANY''')
   result = ""
   for row in rows:
      result += str(row[0])+" is "+str(row[1])+"yo\n"
   return result

if __name__ =='__main__':
   app.run(host='0.0.0.0', port=8080)

