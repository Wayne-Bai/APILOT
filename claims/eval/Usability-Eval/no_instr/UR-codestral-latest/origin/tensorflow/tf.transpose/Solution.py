import tensorflow as tf

# A Tensor to transpose
a = tf.constant([[1, 2],
                 [3, 4],
                 [5, 6]])

# Transposing the Tensor
a_transposed = tf.transpose(a)

print(a_transposed)
