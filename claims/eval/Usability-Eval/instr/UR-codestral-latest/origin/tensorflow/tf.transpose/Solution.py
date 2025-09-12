import tensorflow as tf

# Define a tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor
a_transposed = tf.transpose(a)

# Print the original and transposed tensors
print("Original tensor:\n", a.numpy())
print("Transposed tensor:\n", a_transposed.numpy())
