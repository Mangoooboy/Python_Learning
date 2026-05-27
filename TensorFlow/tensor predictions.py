import tensorflow as tf
import numpy as np

# Training data
x = np.array([[1.0], [2.0], [3.0], [4.0]])
y = np.array([[2.0], [4.0], [6.0], [8.0]])

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compile
model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.01),
    loss='mse'
)

# Train
model.fit(x, y, epochs=1000, verbose=0)

# Predict
prediction = model.predict(np.array([[5.0]]), verbose=0)

print(prediction)