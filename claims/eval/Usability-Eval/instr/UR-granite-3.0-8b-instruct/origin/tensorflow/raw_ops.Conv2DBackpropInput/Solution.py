import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([1, 5, 5, 1])

# Define the filter tensor
filter_tensor = tf.random.normal([3, 3, 1, 1])

# Define the input shape
input_shape = tf.shape(input_tensor)

# Define the filter shape
filter_shape = tf.shape(filter_tensor)

# Define the strides
strides = [1, 1, 1, 1]

# Define the padding
padding = 'SAME'

# Compute the convolution
conv = tf.nn.conv2d(input_tensor, filter_tensor, strides, padding)

# Compute the gradients of convolution with respect to the input
grad_input = tf.nn.conv2d_backprop_input(input_shape, filter_shape, conv, filter_tensor, strides, padding)
