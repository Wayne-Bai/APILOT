import tensorflow as tf
from tensorflow.keras import layers, models

# Dummy data for demonstration purposes
import numpy as np

# Generate some random data
x_train = np.random.rand(1000, 32)
y_train = np.random.randint(0, 10, 1000)

# Build a simple model
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(32,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Define a TensorBoard callback
log_dir = "logs/fit/"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Fit the model with TensorBoard callback
model.fit(x_train, y_train, epochs=5, callbacks=[tensorboard_callback])
