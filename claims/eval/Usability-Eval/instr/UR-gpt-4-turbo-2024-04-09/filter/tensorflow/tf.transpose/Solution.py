import tensorflow as tf

# Tensor 'a'
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor 'a'
a_transposed = tf.linalg.matrix_transpose(a)

print("Original Tensor 'a':")
print(a.numpy())
print("Transposed Tensor 'a':")
print(a_transposed.numpy())
