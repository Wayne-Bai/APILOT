import tensorflow as tf

# Define Tensor 'a'
a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transposes Tensor 'a'
a_transpose = tf.transpose(a)

# Print original and transposed Tensor 'a'
print("Original Tensor 'a':", a)
print("Transposed Tensor 'a':", a_transpose)
