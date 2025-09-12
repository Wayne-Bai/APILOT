import tensorflow as tf

# Assuming 'a' is a tensor
a = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float32)

# Transpose the tensor 'a'
a_transposed = tf.transpose(a, [1, 0])  # transpose along the rows to columns

# Compute the result and print it
print(a_transposed)
