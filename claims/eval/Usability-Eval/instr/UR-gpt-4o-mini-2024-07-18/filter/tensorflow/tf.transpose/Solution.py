import tensorflow as tf

# Assuming 'a' is the input tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor 'a'
transposed_a = tf.transpose(a)

# Print the result
print(transposed_a)
