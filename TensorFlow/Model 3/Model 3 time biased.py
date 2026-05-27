import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# =========================
# LOAD CSV
# =========================

data = pd.read_csv("../CSV file/Esp8266-BMP180.csv")

print(data.head())

# =========================

# Convert Time column to datetime

data["Time"] = pd.to_datetime(data["Time"])

# Extract Hour and Minute

data["Hour"] = data["Time"].dt.hour

data["Minute"] = data["Time"].dt.minute
# CREATE TIME FEATURES
# =========================

# Convert hour + minute into total minutes

minutes_of_day = (
    data["Hour"] * 60
    +
    data["Minute"]
)

# Cyclic encoding

data["sinTime"] = np.sin(
    2 * np.pi * minutes_of_day / 1440
)

data["cosTime"] = np.cos(
    2 * np.pi * minutes_of_day / 1440
)

# =========================
# INPUTS AND OUTPUT
# =========================

X = data[[
    "sinTime",
    "cosTime",
    "Pressure"
]]

y = data["Temperature"]

# =========================
# NORMALIZATION
# =========================

# Only normalize pressure

X["Pressure"] = X["Pressure"] / X["Pressure"].max()

# Normalize temperature

y = y / y.max()

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# BUILD MODEL
# =========================

model = tf.keras.Sequential([

    tf.keras.layers.Dense(
        16,
        activation='relu',
        input_shape=(3,)
    ),

    tf.keras.layers.Dense(
        16,
        activation='relu'
    ),

    tf.keras.layers.Dense(1)

])

# =========================
# COMPILE
# =========================

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# =========================
# TRAIN
# =========================

model.fit(
    X_train,
    y_train,
    epochs=200,
    batch_size=8,
    validation_data=(X_test, y_test)
)

# =========================
# SAVE MODEL
# =========================

model.save(
    "temperature_time_model.keras"
)

print("\nModel Saved!")

# =========================
# CONVERT TO TFLITE
# =========================

converter = tf.lite.TFLiteConverter.from_keras_model(
    model
)

tflite_model = converter.convert()

with open(
        "KL files/temperature_time_model.tflite",
    "wb"
) as f:

    f.write(tflite_model)

print("TFLite Model Saved!")