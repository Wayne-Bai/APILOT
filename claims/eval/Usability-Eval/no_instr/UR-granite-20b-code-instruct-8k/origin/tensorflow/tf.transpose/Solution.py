import tensorflow as tf

# Define a tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor
transposed_a = tf.transpose(a)

# Print the result
print(transposed_a)
