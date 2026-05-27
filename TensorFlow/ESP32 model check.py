import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model(
    "Trained Models/temperature_model2.keras"
)

print("\nModel Loaded Successfully!")

# ================= TEST 1 =================
# Normal realistic input

test_data1 = np.array([
    [15, 30, 909.75, 29.4]
])

# ================= TEST 2 =================
# Wrong pressure test

test_data2 = np.array([
    [15, 30, 850, 29.4]
])

# ================= NORMALIZATION =================
# SAME normalization values used during training

max_values = np.array([23, 59, 913.75, 35])

test_data1 = test_data1 / max_values
test_data2 = test_data2 / max_values

# ================= PREDICTIONS =================

prediction1 = model.predict(test_data1)

prediction2 = model.predict(test_data2)

# ================= PRINT RESULTS =================

print("\n==============================")
print("NORMAL PRESSURE TEST")
print("==============================")

print("Prediction:")
print(prediction1)

print("\n==============================")
print("WRONG PRESSURE TEST")
print("==============================")

print("Prediction:")
print(prediction2)