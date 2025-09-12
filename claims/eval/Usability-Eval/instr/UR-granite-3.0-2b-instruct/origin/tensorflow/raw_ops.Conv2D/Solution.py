import tensorflow as tf

# Define the input and filter tensors
input_tensor = tf.constant([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
filter_tensor = tf.constant([[[1, 0], [0, 1]]])

# Compute the 2-D convolution
convolution = tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor, strides=[1, 1, 1, 1], padding='SAME')

# Print the result
print(convolution)
