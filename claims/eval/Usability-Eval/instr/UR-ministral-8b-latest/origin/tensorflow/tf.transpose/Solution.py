import tensorflow as tf

# Example tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transposing the tensor
transposed = tf.transpose(a)

# Output the transposed tensor
print(transposed.numpy())
