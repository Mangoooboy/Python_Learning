#include <WiFi.h>

char ssid[] = "Airtel_Univision";
char pass[] = "Univision@2026";

void setup() {
  Serial.begin(115200);

  Serial.println();
  Serial.println("Connecting to WiFi...");

  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected!");

  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {

}
