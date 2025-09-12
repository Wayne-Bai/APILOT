import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import datetime

# Set up TensorBoard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Create a simple neural network model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Generate some random data
x_train = np.random.rand(1000, 784)
y_train = np.random.randint(0, 10, size=1000)

# Train the model with TensorBoard visualization
model.fit(x_train, y_train, epochs=10, callbacks=[tensorboard_callback])
