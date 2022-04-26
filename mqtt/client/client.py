from mqtt.config.mqttBrokerInfo import broker, port, client_id, username, password
from paho.mqtt import client as mqtt_client
import json


def connect_mqtt(callback):
    def callback_connect(client, userdata, flags, rc):
        if rc == 0:

            subscribe(client, callback)
            pass
        else:
            print("Failed to connect, return code %d\n", rc)

    print("dang connect")
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = callback_connect
    try:
        client.connect(broker, port)  # connect to broker
    except:
        client.loop_start()
    client.loop_start()
    return client


def subscribe(client, callback):
    def on_message(client, userdata, msg):
        callback(msg.topic, msg.payload.decode())
    client.subscribe("BlueTeam")

    client.on_message = on_message

