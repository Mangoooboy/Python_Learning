import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("Trained Models/temperature_model.keras")

# Get weights and biases
weights = model.get_weights()

# Print everything
for i, w in enumerate(weights):
    print(f"\nLayer {i}:")
    print(w)