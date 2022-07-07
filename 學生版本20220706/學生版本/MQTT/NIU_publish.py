import paho.mqtt.publish as publish
 
host = "192.168.0.10"              # Broker's IP
topic = "NIU"           # Topic
var =1                          # Declare variable
while var ==1: 
	payload = input("Please enter your message:")
	publish.single(topic, payload, qos=1,hostname=host)
