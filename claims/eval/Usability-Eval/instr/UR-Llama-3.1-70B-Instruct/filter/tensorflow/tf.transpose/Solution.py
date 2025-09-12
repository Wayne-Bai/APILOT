# Import necessary libraries
import tensorflow as tf

# Define a tensor
a = tf.constant([[1, 2], [3, 4]])

# Transpose the tensor using tf.transpose()
b = tf.transpose(a)

# Print the original and transposed tensors
print("Original Tensor:")
print(a)
print("Transposed Tensor:")
print(b)
