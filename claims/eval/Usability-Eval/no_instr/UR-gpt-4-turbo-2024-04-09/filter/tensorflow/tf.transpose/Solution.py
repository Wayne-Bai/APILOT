import tensorflow as tf

# Sample tensor 'a'
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor 'a'
transposed_a = tf.linalg.matrix_transpose(a)
# Print the result
print(transposed_a)
