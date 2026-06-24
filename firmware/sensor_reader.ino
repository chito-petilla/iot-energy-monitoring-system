// Simulated IoT Energy Sensor
// Reads voltage and current and sends data to backend API

#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

const char* serverUrl = "http://localhost:5000/api/data";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {

    float voltage = random(210, 240);
    float current = random(1, 10);

    String payload = "{";
    payload += "\"device_id\":\"sensor-001\",";
    payload += "\"voltage\":" + String(voltage) + ",";
    payload += "\"current\":" + String(current);
    payload += "}";

    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    int response = http.POST(payload);

    Serial.println("Response: " + String(response));
    http.end();
  }

  delay(5000);
}
