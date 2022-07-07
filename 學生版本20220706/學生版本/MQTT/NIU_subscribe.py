import paho.mqtt.client as mqtt
import demjson

def on_connect(client, userdata, flags, rc):
    print("connected with result code "+ str(rc))
    client.subscribe("NIU")

def on_message(client, userdata, msg):
    print(msg.topic +" "+ ":" + str(msg.payload, encoding = 'utf-8'))
    message = demjson.decode(str(msg.payload, encoding = "utf-8"))
    print(message)
    print(message['temp'])
    print(message['humid'])



client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.10", 1883, 60)

client.loop_forever()
