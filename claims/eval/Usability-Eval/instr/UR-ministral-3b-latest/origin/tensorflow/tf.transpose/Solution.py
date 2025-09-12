import tensorflow as tf

# Example tensor
a = tf.constant([[1, 2], [3, 4]])

# Transpose tensor 'a'
b = tf.transpose(a, perm=[1, 0])  # Transpose the tensor

# Print the transposed tensor
print(b)
