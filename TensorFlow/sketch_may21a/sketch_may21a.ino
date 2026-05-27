#include "model2.h"
#include <tflm_esp32.h>
#include <eloquent_tinyml.h>

#define NUMBER_OF_INPUTS 4
#define NUMBER_OF_OUTPUTS 1
#define TF_NUM_OPS 4
#define ARENA_SIZE 16 * 1024

// Your model array name from model2.h
#define MODEL_ARRAY model_data

// Replace these with the exact normalization values from Python training.
// If you used StandardScaler:
// normalized = (value - mean) / std
const float HOUR_MEAN = 12.0;
const float HOUR_STD = 6.9;

const float MINUTE_MEAN = 30.0;
const float MINUTE_STD = 17.3;

const float PRESSURE_MEAN = 101325.0;
const float PRESSURE_STD = 500.0;

const float PREV_TEMP_MEAN = 30.0;
const float PREV_TEMP_STD = 5.0;

Eloquent::TF::Sequential<TF_NUM_OPS, ARENA_SIZE> model;

float previousTemperature = 30.0;

float normalizeInput(float value, float mean, float stddev) {
  return (value - mean) / stddev;
}

void setup() {
  Serial.begin(115200);
  delay(3000);

  Serial.println("ESP32 TinyML Temperature Prediction");

  model.setNumInputs(NUMBER_OF_INPUTS);
  model.setNumOutputs(NUMBER_OF_OUTPUTS);

  model.resolver.AddFullyConnected();
  model.resolver.AddRelu();
  model.resolver.AddAdd();
  model.resolver.AddReshape();

  while (!model.begin(MODEL_ARRAY).isOk()) {
    Serial.print("Model init failed: ");
    Serial.println(model.exception.toString());
    delay(1000);
  }

  Serial.println("Model loaded successfully");
}

void loop() {
  // Test values. Later replace these with real BMP180/time values.
  float hour = 14.0;
  float minute = 30.0;
  float pressure = 101250.0;

  float input[NUMBER_OF_INPUTS] = {
    normalizeInput(hour, HOUR_MEAN, HOUR_STD),
    normalizeInput(minute, MINUTE_MEAN, MINUTE_STD),
    normalizeInput(pressure, PRESSURE_MEAN, PRESSURE_STD),
    normalizeInput(previousTemperature, PREV_TEMP_MEAN, PREV_TEMP_STD)
  };

  if (!model.predict(input).isOk()) {
    Serial.print("Inference failed: ");
    Serial.println(model.exception.toString());
    delay(2000);
    return;
  }

  float predictedTemperature = model.output(0);
  previousTemperature = predictedTemperature;

  Serial.print("Predicted temperature: ");
  Serial.println(predictedTemperature, 4);

  Serial.print("Inference time: ");
  Serial.print(model.benchmark.microseconds());
  Serial.println(" us");

  delay(2000);
}
