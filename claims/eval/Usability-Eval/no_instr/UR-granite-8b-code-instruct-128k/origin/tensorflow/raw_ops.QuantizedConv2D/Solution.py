import tensorflow as tf

# Define the input and filter tensors
input = tf.constant([[[[1.0, 2.0], [3.0, 4.0]]], [[[5.0, 6.0], [7.0, 8.0]]]])
filter = tf.constant([[[[1.0, 0.0], [0.0, -1.0]]], [[[-1.0, 0.0], [0.0, 1.0]]]])

# Use the tf.raw_ops.QuantizedConv2D method to compute the convolution
result = tf.raw_ops.QuantizedConv2D(input=input, filter=filter, min_input=0.0, max_input=10.0, min_filter=0.0, max_filter=10.0, strides=[1, 1, 1, 1], padding='SAME', dilations=[1, 1, 1, 1])

# Print the result
print(result)
