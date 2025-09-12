import tensorflow as tf

# Define a 2D tensor
a = tf.constant([[1, 2], [3, 4], [5, 6]])

# Transpose the tensor
transposed_a = tf.transpose(a)

# Print the original and transposed tensors
print("Original Tensor:\n", a.numpy())
print("Transposed Tensor:\n", transposed_a.numpy())
