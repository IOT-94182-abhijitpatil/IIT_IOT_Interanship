import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temperature = round(random.uniform(20, 35), 2)
    intensity = round(random.uniform(100, 800), 2)

    client.publish("sensor/lm35", temperature)
    client.publish("sensor/ldr", intensity)

    print("Temperature:", temperature)
    print("Light Intensity:", intensity)

    time.sleep(5)
