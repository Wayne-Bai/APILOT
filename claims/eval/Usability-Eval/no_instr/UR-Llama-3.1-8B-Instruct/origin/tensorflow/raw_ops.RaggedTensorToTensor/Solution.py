# Importing the necessary TensorFlow libraries
import tensorflow as tf
import numpy as np

# Creating a random ragged tensor
ragged_tensor = tf.RaggedTensor.from_row_lengths(
    [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]],
    [3, 2, 4, 1]
)

print("Ragged Tensor: ", ragged_tensor)

# Reshaping the ragged tensor into a dense tensor
dense_tensor = tf.ragged.ragged_serialize(ragged_tensor)

print("Reshaped Dense Tensor: ", dense_tensor)
