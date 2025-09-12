# Import tensorflow library
import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal((1, 28, 28, 1))

# Define the filter tensor
filter_tensor = tf.random.normal((5, 5, 1, 32))

# Define the strides tensor
strides = [1, 1, 1, 1]

# Define the padding tensor
padding = 'SAME'

# Define the dilation_rate tensor
dilation_rate = [1, 1]

# Compute the 2-D convolution using tf.nn.conv2d
output = tf.nn.conv2d(input=input_tensor, filters=filter_tensor, strides=strides, padding=padding, dilation_rate=dilation_rate)

# Print the output shape
print(tf.shape(output))
