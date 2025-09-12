import tensorflow as tf

# Define a tensor a
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose a
a_transposed = tf.transpose(a)

# Print the result
print(a_transposed)
