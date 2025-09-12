import tensorflow as tf

# Create a sample tensor 'a'
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor 'a'
transposed_a = tf.linalg.transpose(a)

# Print the transposed tensor
print(transposed_a)
