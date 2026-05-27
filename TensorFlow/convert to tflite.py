import tensorflow as tf

# Load trained Keras model
model = tf.keras.models.load_model("Trained Models/temperature_model.keras")

# Create converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Convert model
tflite_model = converter.convert()

# Save converted model
with open("Trained Models/temperature_model.tflite", "wb") as f:
    f.write(tflite_model)

print("TFLite model created successfully!")