import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
                             [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]], dtype=tf.float32)

# Define the filter tensor
filter_tensor = tf.constant([[1, 1], [1, 1]], dtype=tf.float32)

# Perform the 2D convolution operation
conv2d_tensor = tf.raw_ops.Conv2D(input=input_tensor, filters=filter_tensor, strides=[1, 1, 1, 1], padding='VALID')

# Print the resulting tensor
print(conv2d_tensor)
