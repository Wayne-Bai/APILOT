import tensorflow as tf

# Assuming 'a' is a TensorFlow tensor
a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transpose the tensor using tf.transpose()
a_transposed = tf.transpose(a)

# Print the transposed tensor
print(a_transposed)
