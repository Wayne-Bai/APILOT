# Import the tensorflow library
import tensorflow as tf

# Create a tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Print the original tensor
print("Original Tensor:")
print(a)

# Use tf.transpose to transpose the tensor
transposed_a = tf.transpose(a)

# Print the transposed tensor
print("\nTransposed Tensor:")
print(transposed_a)
