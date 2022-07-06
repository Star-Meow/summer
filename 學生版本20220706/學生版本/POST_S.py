#模擬POST傳輸
# 引入 random ,requests,time
import random
import requests
import time
#產生介於 0.0 到 100.0 之間的隨機浮點數
#並取到小數第二位
while(True):
    # 產生介於 0.0 到 100.0 之間的隨機浮點數
    temp = round(random.uniform(0.0, 100.0),2)
    humid = round(random.uniform(0.0, 100.0),2)
    #將數值做成JSON格式
    json_data = {'temp': temp, 'humid': humid}
    # 使用 POST 方式
    r = requests.post('http://127.0.0.1:5000/NIUPOST',json=json_data)
    #暫停2秒
    time.sleep(2)