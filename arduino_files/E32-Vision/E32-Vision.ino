/*
  Complete details at https://RandomNerdTutorials.com/esp32-useful-wi-fi-functions-arduino/
*/

//Testing wifi

#include <WiFi.h>

// Replace with your network credentials (STATION)
const char* ssid     = "nombre_red";
const char* password = "contraseña";

void setup(){
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  delay(100);
}

void loop(){
  Serial.print("RSSI: ");
  Serial.println(WiFi.RSSI());
  delay(2000);
}
