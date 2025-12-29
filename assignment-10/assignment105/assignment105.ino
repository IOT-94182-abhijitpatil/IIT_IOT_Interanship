#include <WiFi.h>
#include <HTTPClient.h>
#include<ArduinoMqttClient.h>
#include <DHT.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *host = "172.18.4.35";
unsigned int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi ");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}

void loop() {

  float hum = dht.readHumidity();

  // check sensor read
  if (isnan(hum)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  String body = "{\"humidity\":" + String(hum) + "}";

  WiFiClient wifiClient;
  HTTPClient httpClient;
  MqttClient publisher(wifiClient);

   if(publisher.connect(host, port)){
    publisher.beginMessage("alert");
    if(hum>70){
      publisher.print("humidity is above threshold");
      
    }
    else{
      publisher.print("humidity is within range");
      
    }
    publisher.endMessage();
   }

    
  

  httpClient.begin(wifiClient, "http://172.18.4.35:4000/humidity");
  httpClient.addHeader("Content-Type", "application/json");

  int status = httpClient.POST(body);

  Serial.printf("status = %d\n", status);
  Serial.println(body);

  httpClient.end();

  delay(6000);
}
