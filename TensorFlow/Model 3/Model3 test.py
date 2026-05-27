import tensorflow as tf
import numpy as np
import pandas as pd

# =========================
# LOAD MODEL
# =========================

model = tf.keras.models.load_model(
    "KL files/temperature_time_model.keras"
)

print("Model Loaded!")

# =========================
# LOAD CSV
# =========================

data = pd.read_csv("../CSV file/Esp8266-BMP180.csv")

# =========================
# GET MAX VALUES
# =========================

max_pressure = data["Pressure"].max()

max_temp = data["Temperature"].max()

# =========================
# TEST INPUT
# =========================

# Example:
# 3:30 PM

hour = 15
minute = 30

# Convert to minutes

minutes_of_day = (
    hour * 60
    +
    minute
)

# Cyclic encoding

sinTime = np.sin(
    2 * np.pi * minutes_of_day / 1440
)

cosTime = np.cos(
    2 * np.pi * minutes_of_day / 1440
)

# Example pressure

pressure = 909.75

# Normalize pressure

pressure = pressure / max_pressure

# =========================
# CREATE INPUT
# =========================

test_input = np.array([[
    sinTime,
    cosTime,
    pressure
]])

# =========================
# PREDICT
# =========================

prediction = model.predict(test_input)

# Convert back to real temperature

predicted_temp = (
    prediction[0][0]
    * max_temp
)

# =========================
# PRINT RESULTS
# =========================

print("\n====================")
print("MODEL TEST")
print("====================")

print("\nTime:")

print(f"{hour}:{minute}")

print("\nPressure:")

print(pressure * max_pressure)

print("\nPredicted Temperature:")

print(predicted_temp)