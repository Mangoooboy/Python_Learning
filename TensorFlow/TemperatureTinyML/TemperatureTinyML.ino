#include "model2.h"

#include <Wire.h>
#include <Adafruit_BMP085.h>

#include <tflm_esp32.h>
#include <eloquent_tinyml.h>

// =======================
// BMP180 Sensor
// =======================

Adafruit_BMP085 bmp;

// =======================
// TinyML Settings
// =======================

#define INPUTS 4
#define OUTPUTS 1
#define TENSOR_ARENA_SIZE 16 * 1024
#define TF_OPS 4

Eloquent::TF::Sequential<
  TF_OPS,
  TENSOR_ARENA_SIZE
> model;

// =======================
// Previous Temperature
// =======================

float previousTemp = 29.4;

// =======================
// Setup
// =======================

void setup() {

  Serial.begin(115200);

  // Start BMP180
  if (!bmp.begin()) {

    Serial.println("BMP180 NOT FOUND!");

    while (1);
  }

  Serial.println("BMP180 Connected!");

  // TinyML setup
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

  // Read BMP180
  float pressure = bmp.readPressure() / 100.0;

  float realTemp = bmp.readTemperature();

  // Temporary test time
  float hour = 15.0;
  float minute = 30.0;

  // =======================
  // Normalize Inputs
  // =======================

  float input[INPUTS];

  input[0] = hour / 23.0;

  input[1] = minute / 59.0;

  input[2] = pressure / 913.75;

  input[3] = previousTemp / 35.0;

  // =======================
  // Predict
  // =======================

  if (!model.predict(input).isOk()) {

    Serial.print("Inference Failed: ");
    Serial.println(model.exception.toString());

    delay(2000);
    return;
  }

  float prediction = model.output(0);

  // =======================
  // Print Results
  // =======================

  Serial.println("====================");

  Serial.print("Real Temp: ");
  Serial.println(realTemp);

  Serial.print("Pressure: ");
  Serial.println(pressure);

  Serial.print("Predicted Temp: ");
  Serial.println(prediction);

  // Update previous temp
  previousTemp = prediction;

  delay(3000);
}
