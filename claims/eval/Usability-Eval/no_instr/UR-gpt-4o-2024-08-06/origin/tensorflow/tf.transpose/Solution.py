import tensorflow as tf

# Create a sample tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor
a_transposed = tf.transpose(a)

# Print the original and transposed tensors
print("Original Tensor:")
print(a.numpy())
print("\nTransposed Tensor:")
print(a_transposed.numpy())
