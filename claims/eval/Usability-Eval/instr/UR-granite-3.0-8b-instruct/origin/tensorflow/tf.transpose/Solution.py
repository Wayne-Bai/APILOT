import tensorflow as tf

# Assuming 'a' is a Tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the Tensor 'a'
transpose_a = tf.transpose(a)

print(transpose_a)
