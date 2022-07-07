#include <LWiFi.h>
#include "DHT.h"

char _lwifi_ssid[] = "voip 406";          //wifi Ac
char _lwifi_pass[] = "voipvoip";       //wifi Pa
DHT __dht3(3,DHT11);                     //建立濕度感測器 設置腳位 型號
WiFiClient client;                       //建立wifi用戶端物件

void setup() {
  Serial.begin(9600);                   //設定板子跟電腦的溝通頻率 下面那條是接wifi
  while(WiFi.begin(_lwifi_ssid, _lwifi_pass) != WL_CONNECTED)  {delay(1000);}
  Serial.print(WiFi.localIP().toString()); //印出7696的IP
  __dht3.begin();                       //啟動濕度感測器
}

void loop() {
  String h = (String) __dht3.readHumidity();       //抓濕度
  String t = (String) __dht3.readTemperature();    //抓溫度
  String jsonStr = "{\"temp\":"+t+",\"humid\":"+h+"}"; //串接json字串
  delay(2000);         
  httpSend(jsonStr);                                   //使用HttpSend函數 使用JSONStr填入參數 
}

void httpSend(String jsonStr){
   if (client.connect("192.168.0.10", 5000))       //與python建立連線
   {
      Serial.println("connected to sever (POST)"); 
      client.print("POST /NIUGET HTTP/1.1\r\n");       //發送POST格式內容
      client.print("Content-Type: application/json\n");//發送資料內容的格式
      client.print("Content-Length:");                 //發送資料內容的長度
      client.print(jsonStr.length());
      client.print("\n\n");
      client.print(jsonStr);                           //資料內容
      client.stop();                                   //掐斷連線
      delay(10);
    }
  }


