import pandas as pd
import tensorflow as tf
import numpy as np

# Load CSV
data = pd.read_csv("CSV file/Esp8266-BMP180.csv")

# Convert Time column
data['Time'] = pd.to_datetime(data['Time'])

# Extract Hour and Minute
data['Hour'] = data['Time'].dt.hour
data['Minute'] = data['Time'].dt.minute

# Create Previous Temperature column
data['PrevTemp'] = data['Temperature'].shift(1)

# Remove first empty row
data = data.dropna()

# Inputs
X = data[['Hour', 'Minute', 'Pressure', 'PrevTemp']].values

# Output
y = data['Temperature'].values

# Save max values
max_values = X.max(axis=0)

# Normalize inputs
X = X / max_values

# Build Neural Network
model = tf.keras.Sequential([

    tf.keras.layers.Input(shape=(4,)),

    tf.keras.layers.Dense(16, activation='relu'),

    tf.keras.layers.Dense(1)

])

# Compile
model.compile(
    optimizer='adam',
    loss='mse'
)

# Train
model.fit(X, y, epochs=200)

# Save model
model.save("temperature_model2.keras")

print("\nModel Saved Successfully!")

# ================= TEST =================

# Test input:
# Hour, Minute, Pressure, PreviousTemp

test_data = np.array([
    [15, 30, 909.75, 29.4]
])

# Normalize
test_data = test_data / max_values

# Predict
prediction = model.predict(test_data)

print("\nPredicted Temperature:")
print(prediction)