

import sqlite3
from flask import g
from flask import Flask
from flask import request

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



@app.route('/show')
def show():
   filename = request.args.get('filename', type=str)
   try:
      with open(filename) as f:
         content = f.read().replace('\n' , '<br>\n' )
   except:
      content = filename + " : Unable to read the file!" 
   return content

if __name__ =='__main__':
   app.run(host='0.0.0.0', port=8080)




