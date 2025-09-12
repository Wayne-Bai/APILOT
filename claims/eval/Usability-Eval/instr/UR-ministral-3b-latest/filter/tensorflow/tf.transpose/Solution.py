import tensorflow as tf

# Example Tensor
a = tf.random.normal((2, 3))

# Transpose the tensor
transposed_a = tf.transpose(a)

print(transposed_a)
