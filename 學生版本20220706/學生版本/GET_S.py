#模擬GET傳輸
# 引入 random ,requests,time
import random
import requests#需安裝 pip install requests
import time
#產生介於 0.0 到 100.0 之間的隨機浮點數
#並取到小數第二位
while(True):
    # 產生介於 0.0 到 100.0 之間的隨機浮點數
    temp = round(random.uniform(0.0, 100.0),2)
    humid = round(random.uniform(0.0, 100.0),2)
    # 使用 GET 方式
    r = requests.get('http://127.0.0.1:5000/NIUGET?temp='+str(temp)+'&humid='+str(humid))
    #暫停2秒
    time.sleep(2)