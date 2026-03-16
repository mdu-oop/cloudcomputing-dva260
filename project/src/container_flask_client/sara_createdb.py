import sqlite3

conn = sqlite3.connect('sensors.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.executescript("""CREATE TABLE IF NOT EXISTS sensors(
   sensor_id INTEGER PRIMARY KEY,
   sensor_type TEXT NOT NULL,
   location_id INTEGER NOT NULL,
   unit TEXT NOT NULL,
   FOREIGN KEY (location_id) REFERENCES locations(location_id));

   CREATE TABLE IF NOT EXISTS measurements(
   sensor_id INTEGER NOT NULL,
   timestamp TEXT NOT NULL,
   value REAL NOT NULL,
   FOREIGN KEY(sensor_id) REFERENCES sensors(sensor_id));

   CREATE TABLE IF NOT EXISTS locations(
   location_id INTEGER PRIMARY KEY,
   latitude REAL NOT NULL,
   longitude REAL NOT NULL);
   """)

cursor.executescript("""CREATE VIEW IF NOT EXISTS sensor_data
                  AS
                  SELECT
                  sensors.sensor_id AS sensor_id,
                  sensors.sensor_type AS sensor_type,
                  sensors.unit AS unit,
                  locations.latitude AS latitude,
                  locations.longitude AS longitude,
                  measurements.timestamp AS timestamp,
                  measurements.value AS value

                  FROM sensors
                  INNER JOIN measurements ON measurements.sensor_id = sensors.sensor_id
                  INNER JOIN locations ON sensors.location_id = locations.location_id;
                  """)

conn.commit()
conn.close()