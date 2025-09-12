import tensorflow as tf

# Enable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_experimental_options({"mlir_bridge": True})

# Example usage of TensorFlow
# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Print model summary
model.summary()
