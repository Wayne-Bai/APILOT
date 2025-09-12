import tensorflow as tf
import numpy as np

# Create a Tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Transpose the Tensor
transposed_tensor = tf.transpose(tensor)

# Print the Transposed Tensor
print(transposed_tensor)
