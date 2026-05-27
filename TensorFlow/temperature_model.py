import pandas as pd
import tensorflow as tf
import numpy as np

# Load CSV file
data = pd.read_csv("CSV file/Esp8266-BMP180.csv")

# Convert Time column to datetime
data['Time'] = pd.to_datetime(data['Time'])

# Extract Hour and Minute
data['Hour'] = data['Time'].dt.hour
data['Minute'] = data['Time'].dt.minute

# Inputs (features)
X = data[['Hour', 'Minute', 'Pressure']].values

# Output (label)
y = data['Temperature'].values

# Save max values for normalization
max_values = X.max(axis=0)

# Normalize inputs
X = X / max_values

# Build Neural Network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile Model
model.compile(
    optimizer='adam',
    loss='mse'
)

# Train Model
model.fit(X, y, epochs=100)

# Save model
model.save("temperature_model.keras")

print("\nModel Saved Successfully!")

# Test input
test_data = np.array([[15, 30, 909.75]])

# Normalize test input
test_data = test_data / max_values

# Predict
prediction = model.predict(test_data)

print("\nPredicted Temperature:")
print(prediction)