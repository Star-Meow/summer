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
void callback(char* topic, byte* payload, unsigned int length);
void setup() {
  // put your setup code here, to run once:
 
}

void loop() {
  // put your main code here, to run repeatedly:
 
}
void connectMQTT() {
 
}
void callback(char* topic, byte* payload, unsigned int length) {   //MQTT Relay
  
}
