#include <LWiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#define MQTT_SUB_TOPIC "NIU"
#define MQTT_SUB_TOPIC_1 "NIU_1"
#define MQTT_SERVER_IP ""
#define MQTT_SERVER_PORT 1883
#define MQTT_CLIENT_ID ""
char _lwifi_ssid[] = "";
char _lwifi_pass[] = "";
DHT __dht3(, );
WiFiClient mqttClient;
PubSubClient client(mqttClient);

void setup() {
  // put your setup code here, to run once:
 
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
void connectMQTT() {
   // Loop until we're reconnected
  while (!client.connected())
  {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(MQTT_CLIENT_ID))
    {
      Serial.println("connected");
      client.subscribe(MQTT_SUB_TOPIC_1);
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

