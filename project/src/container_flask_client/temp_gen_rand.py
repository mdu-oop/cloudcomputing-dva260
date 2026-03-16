import sqlite3
import urllib.parse
import urllib.request
import random
from time import sleep
from datetime import datetime, timezone

DATABASE = 'sensors.db'

base = 'http://127.0.0.1:8080/store'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

sensor_id = 1
location_id = 1
sensor_type = 'temp'
unit = '°C'
latitude = 59.3293
longitude = 18.0686

conn = sqlite3.connect(DATABASE)
conn.execute("PRAGMA foreign_keys = ON")

conn.execute('''INSERT OR IGNORE INTO locations (location_id, latitude, longitude)
                VALUES (?, ?, ?)''',
             (location_id, latitude, longitude))

conn.execute('''INSERT OR IGNORE INTO sensors (sensor_id, sensor_type, location_id, unit)
                VALUES (?, ?, ?, ?)''',
             (sensor_id, sensor_type, location_id, unit))

conn.commit()
conn.close()

while True:
    temp_rand = random.randint(-30, 30)

    values = {
        'value': str(temp_rand),
        'sensor_id': str(sensor_id),
        'timestamp': datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    }

    url = base + '?' + urllib.parse.urlencode(values)
    req = urllib.request.Request(url, headers=headers)

    sleep(1)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(response.status, the_page.decode('utf-8'))