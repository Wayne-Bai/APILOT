
import tensorflow as tf

# Define a tensor "a"
a = tf.constant([[1, 2], [3, 4]])

# Perform the transpose on "a" using tf.transpose
b = tf.transpose(a)

# Print the result
print(b)
