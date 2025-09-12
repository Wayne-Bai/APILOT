
import tensorflow as tf
from tensorflow import keras

# Define the optimizer using the Keras optimizer class
opt = keras.optimizers.Adam(learning_rate=0.001)

# Create a model with two dense layers and an output layer
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model with the optimizer and a loss function
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
