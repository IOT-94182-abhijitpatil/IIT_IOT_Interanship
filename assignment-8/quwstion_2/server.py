import paho.mqtt.client as mqtt
import mysql.connector
import json

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    device = data["device"]
    status = data["status"]

    sql = "INSERT INTO appliance_status(device_name, status) VALUES (%s, %s)"
    cursor.execute(sql, (device, status))
    db.commit()

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)
client.subscribe("home/appliance/status")
client.on_message = on_message

client.loop_forever()
