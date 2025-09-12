import tensorflow as tf

# Create a tensor
a = tf.constant([[1, 2], [3, 4], [5, 6]])

# Perform transpose operation
a_transpose = tf.transpose(a)

# Print the original tensor and the transposed tensor
print("Original Tensor:")
print(a)
print("\nTransposed Tensor:")
print(a_transpose)
