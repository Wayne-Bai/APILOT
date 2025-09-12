import tensorflow as tf
from tensorflow import keras

# Define input tensors
input_1 = tf.keras.Input(shape=(None,), dtype=tf.float32)
input_2 = tf.keras.Input(shape=(None,), dtype=tf.float32)

# Multiply the inputs element-wise
output = input_1 * input_2

# Define a Keras model from the output tensor
model = keras.Model(inputs=[input_1, input_2], outputs=output)
