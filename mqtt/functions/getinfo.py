# python3.6
from mqtt.functions.teaminfo import setInfo
from mqtt.config.mqttBrokerInfo import broker, port, username, password
from paho.mqtt import client as mqtt_client


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            pass
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client("new_client_2")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    try:
        client.connect(broker, port)  # connect to broker
    except:
        client.loop_start()
    client.connect(broker, port)
    return client


data = []


def subscribe(topic):
    client = connect_mqtt()

    def on_message(client, userdata, msg):
        setInfo(msg.payload)

    client.subscribe(topic)
    client.on_message = on_message
    client.loop_start()
