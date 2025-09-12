import tensorflow as tf

# Enable experimental MLIR-based optimizations by configuring the session
tf.config.optimizer.set_experimental_options({'enable_mlir': True})

# Example model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(32,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Sample data
import numpy as np
x_train = np.random.rand(1000, 32).astype(np.float32)
y_train = np.random.randint(0, 10, size=(1000,))

# Train the model
model.fit(x_train, y_train, epochs=5)
