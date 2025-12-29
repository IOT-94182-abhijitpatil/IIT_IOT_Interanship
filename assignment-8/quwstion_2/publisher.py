import paho.mqtt.publish as publish
import json

data = {
    "device": "LIGHT1",
    "status": "ON"
}

publish.single("home/appliance/control",
               json.dumps(data),
               hostname="broker.hivemq.com")
