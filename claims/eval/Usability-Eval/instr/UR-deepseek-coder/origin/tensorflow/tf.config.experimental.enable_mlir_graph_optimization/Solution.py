import tensorflow as tf

# Enable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer.set_experimental_options({"mlir_bridge": True})

# Example model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Example data
import numpy as np
data = np.random.random((1000, 784))
labels = np.random.randint(10, size=(1000, 1))

# Train the model
model.fit(data, labels, epochs=5, batch_size=32)
