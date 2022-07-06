import paho.mqtt.client as mqtt
import datetime,sqlite3
import demjson
DB_File = ""
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("")
def on_message(client, userdata, msg):

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("", , )
client.loop_forever()