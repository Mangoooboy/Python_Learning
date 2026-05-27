import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model(
    "Trained Models/temperature_model2.keras"
)

print("Model Loaded!")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

# Save TFLite file
with open(
    "Trained Models/temperature_model2.tflite",
    "wb"
) as f:

    f.write(tflite_model)

print("TFLite model created successfully!")