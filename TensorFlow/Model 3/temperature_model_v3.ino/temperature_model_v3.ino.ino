#include "model3.h"

#include <Wire.h>
#include <RTClib.h>
#include <Adafruit_BMP085.h>

#include <tflm_esp32.h>
#include <eloquent_tinyml.h>

#include <math.h>

// =======================
// RTC + BMP180
// =======================

RTC_DS3231 rtc;

Adafruit_BMP085 bmp;

// =======================
// TinyML Settings
// =======================

#define INPUTS 3
#define OUTPUTS 1

#define TENSOR_ARENA_SIZE 16 * 1024

#define TF_OPS 4

Eloquent::TF::Sequential<
  TF_OPS,
  TENSOR_ARENA_SIZE
> model;

// =======================
// Setup
// =======================

void setup() {

  Serial.begin(115200);

  // Start I2C
  Wire.begin(21, 22);

  // =======================
  // RTC
  // =======================

  if (!rtc.begin()) {

    Serial.println("RTC NOT FOUND!");

    while (1);
  }

  Serial.println("RTC Connected!");

  // =======================
  // BMP180
  // =======================

  if (!bmp.begin()) {

    Serial.println("BMP180 NOT FOUND!");

    while (1);
  }

  Serial.println("BMP180 Connected!");

  // =======================
  // TinyML Model
  // =======================

  model.setNumInputs(INPUTS);

  model.setNumOutputs(OUTPUTS);

  model.resolver.AddFullyConnected();

  model.resolver.AddRelu();

  model.resolver.AddAdd();

  model.resolver.AddReshape();

  while (!model.begin(model_data).isOk()) {

    Serial.print("Model Error: ");

    Serial.println(model.exception.toString());

    delay(1000);
  }

  Serial.println("TinyML Model Loaded!");
}

// =======================
// Loop
// =======================

void loop() {

  // =======================
  // Get RTC Time
  // =======================

  DateTime now = rtc.now();

  int hour = now.hour();

  int minute = now.minute();

  // =======================
  // Convert to Minutes
  // =======================

  int minutesOfDay = (

    hour * 60

    +

    minute
  );

  // =======================
  // Cyclic Time Encoding
  // =======================

  float sinTime = sin(
    2 * PI * minutesOfDay / 1440.0
  );

  float cosTime = cos(
    2 * PI * minutesOfDay / 1440.0
  );

  // =======================
  // Read Pressure
  // =======================

  float pressure = bmp.readPressure() / 100.0;

  // =======================
  // Normalize Pressure
  // SAME as Python training
  // =======================

  float normalizedPressure = (
    pressure / 913.75
  );

  // =======================
  // Create Input
  // =======================

  float input[INPUTS] = {

    sinTime,

    cosTime,

    normalizedPressure
  };

  // =======================
  // Run Inference
  // =======================

  if (!model.predict(input).isOk()) {

    Serial.print("Inference Failed: ");

    Serial.println(model.exception.toString());

    delay(2000);

    return;
  }

  // =======================
  // Get Prediction
  // =======================

  float prediction = model.output(0);

  // Convert back to real temperature

  float predictedTemperature = (
    prediction * 35.0
  );

  // =======================
  // Display Results
  // =======================

  Serial.println("====================");

  Serial.print("Time: ");

  Serial.print(hour);

  Serial.print(":");

  Serial.println(minute);

  Serial.print("Pressure: ");

  Serial.print(pressure);

  Serial.println(" hPa");

  Serial.print("Predicted Temperature: ");

  Serial.print(predictedTemperature);

  Serial.println(" C");

  Serial.print("Inference Time: ");

  Serial.print(model.benchmark.microseconds());

  Serial.println(" us");

  delay(3000);
}
