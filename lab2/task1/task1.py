
from flask import g
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/now_<username>')
def show_data(username):

   result = username + ", "
   result += datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   return result

if __name__ =='__main__':
   app.run(host='0.0.0.0', port=8080)

