#include <Wire.h>

void setup() {

  Wire.begin(21, 22);

  Serial.begin(115200);

  Serial.println("Scanning...");

  byte error, address;

  int devices = 0;

  for(address = 1; address < 127; address++ ) {

    Wire.beginTransmission(address);

    error = Wire.endTransmission();

    if (error == 0) {

      Serial.print("I2C Device Found at: 0x");

      Serial.println(address, HEX);

      devices++;
    }
  }

  if (devices == 0) {

    Serial.println("No I2C Devices Found");
  }
  
void loop()
{
  delay(3000);
}
