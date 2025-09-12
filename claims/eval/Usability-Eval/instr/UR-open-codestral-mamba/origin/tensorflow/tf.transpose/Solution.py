import tensorflow as tf

# Assume 'a' is a 2D tensor
a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

a_transposed = tf.transpose(a)

print(a_transposed)
