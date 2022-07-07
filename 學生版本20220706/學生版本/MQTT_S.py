#模擬MQTT傳輸
# 引入 random ,requests,time
# 引入paho.mqtt.publish
import random
import requests
import time
import paho.mqtt.publish as publish
host = "127.0.0.1"# Broker's IP
topic = "NIU"# Topic
#產生介於 0.0 到 100.0 之間的隨機浮點數
#並取到小數第二位
while(True):
    # 產生介於 0.0 到 100.0 之間的隨機浮點數
    temp = round(random.uniform(0.0, 100.0),2)
    humid = round(random.uniform(0.0, 100.0),2)
    #將數值做成JSON格式
    json_data = "{'temp':"+ str(temp)+", 'humid':"+ str(humid)+"}"
    # 使用 MQTT 方式
    publish.single(topic, json_data, qos=1, hostname=host)
    #暫停5秒   
    time.sleep(5)
    