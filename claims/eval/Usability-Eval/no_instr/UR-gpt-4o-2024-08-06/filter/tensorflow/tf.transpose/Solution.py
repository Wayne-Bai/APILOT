import tensorflow as tf

# Create a sample Tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the Tensor
a_transposed = tf.transpose(a)

# Print the original and transposed Tensor
print("Original Tensor:")
print(a.numpy())
print("\nTransposed Tensor:")
print(a_transposed.numpy())
