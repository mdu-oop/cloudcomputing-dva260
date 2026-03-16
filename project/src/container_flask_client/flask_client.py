import sqlite3
from flask import g
from flask import Flask, request, Response
from datetime import datetime


DATABASE = 'sensors.db'

def get_db():
   db = getattr(g,'_database', None)
   if db is None:
     db = g._database = sqlite3.connect(DATABASE)
     db.execute("PRAGMA foreign_keys = ON")
   return db

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
   db = getattr(g,'_database', None)
   if db is not None:
      db.close()

@app.route('/store')
def store_data():
   sensor_id = request.args.get('sensor_id', type=int)
   timestamp = request.args.get('timestamp', type=str)
   value = request.args.get('value', type=float)

   if sensor_id is None or timestamp is None or value is None:
      return "Missing sensor_id, timestamp, or value", 400

   conn = get_db()
   conn.execute(
      "INSERT INTO measurements (sensor_id, timestamp, value) VALUES (?, ?, ?)",
      (sensor_id, timestamp, value)
   )
   conn.commit()

   result = "Value " + str(value) + " stored: " + str(timestamp) + " for sensor " + str(sensor_id)
   return result

@app.route('/fetch')
def fetch_data():
    sensor_type = request.args.get('type')

    if sensor_type is None:
        return "Missing type", 400

    result = ""
    conn = get_db()

    for row in conn.execute('''SELECT sensor_id, sensor_type, unit, latitude, longitude, timestamp, value
                               FROM sensor_data
                               WHERE sensor_type = ?''', (sensor_type,)):
        result += "sensor " + str(row[0]) + " (" + str(row[1]) + ")" + \
                  " measured " + str(row[6]) + " " + str(row[2]) + \
                  " at " + str(row[5]) + \
                  " at location (" + str(row[3]) + ", " + str(row[4]) + ")\n"

    return Response(
        result,
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment; filename=measurements.txt"}
    )

if __name__ =='__main__':
   app.run(host='0.0.0.0', port=8080)