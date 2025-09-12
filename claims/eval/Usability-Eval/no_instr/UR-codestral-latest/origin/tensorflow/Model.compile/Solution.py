# Importing required libraries
import tensorflow as tf
from tensorflow.keras import layers

# Creating a sequential model
model = tf.keras.Sequential()

# Adding layers to the model
# This is an example with a simple network: one input layer, one hidden layer, and one output layer
model.add(layers.Dense(units=64, activation='relu', input_shape=(input_size,)))
model.add(layers.Dense(units=10, activation='softmax'))

# Configuring the model for training
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
