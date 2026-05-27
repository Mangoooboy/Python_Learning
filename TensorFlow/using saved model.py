import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("Trained Models/temperature_model.keras")

# SAME max values used during training
max_values = np.array([23, 59, 910])

# Test input
test_data = np.array([[3, 45, 909.80]])

# Normalize input
test_data = test_data / max_values

# Predict
prediction = model.predict(test_data)

print(prediction)

print(model.predict(np.array([[2, 0, 909.75]]) / max_values))

print(model.predict(np.array([[23, 0, 909.75]]) / max_values))