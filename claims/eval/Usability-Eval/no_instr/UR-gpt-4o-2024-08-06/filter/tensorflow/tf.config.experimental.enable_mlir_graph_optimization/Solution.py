import tensorflow as tf

# Enable experimental MLIR-based TensorFlow Compiler optimizations
tf.config.optimizer.set_experimental_options({'mlir': True})

# Example: Create a simple model to demonstrate that optimizations are enabled
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(784,), activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Generate some dummy data
import numpy as np
x_train = np.random.randn(1000, 784).astype('float32')
y_train = np.random.randint(0, 10, (1000,), dtype='int32')

# Train the model
model.fit(x_train, y_train, epochs=5)
