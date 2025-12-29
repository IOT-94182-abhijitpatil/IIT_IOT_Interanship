import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    value = float(msg.payload.decode())

    if msg.topic == "sensor/lm35":
        sensor = "Temperature"
    else:
        sensor = "Light Intensity"

    query = """
    INSERT INTO sensor_readings (sensor_type, value, timestamp)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor, value, datetime.now()))
    db.commit()

    print(f"Stored {sensor}: {value}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("sensor/lm35")
client.subscribe("sensor/ldr")
client.on_message = on_message

print("Subscriber running...")
client.loop_forever()
