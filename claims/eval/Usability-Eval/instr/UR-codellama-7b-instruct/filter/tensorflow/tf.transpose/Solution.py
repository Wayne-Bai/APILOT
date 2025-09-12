import tensorflow as tf

# Define the tensor to transpose
a = tf.constant([[1, 2], [3, 4]])

# Transpose the tensor
b = tf.transpose(a)

print(b.numpy()) # Output: [[1 3]
               #           [2 4]]
