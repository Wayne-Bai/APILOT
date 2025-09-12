import tensorflow as tf

# Example tensor 'a'
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose of tensor 'a'
a_transposed = tf.linalg.matrix_transpose(a)

print("Original Tensor:\n", a.numpy())
print("Transposed Tensor:\n", a_transposed.numpy())
