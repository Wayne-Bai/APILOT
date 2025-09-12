# Import the necessary tensorflow modules
import tensorflow as tf
import numpy as np

# Create some sample data for the input tensor (batch, height, width, channels)
input_tensor = np.random.rand(1, 28, 28, 1).astype(np.float32)

# Create some sample data for the filter tensor (filter_height, filter_width, in_channels, out_channels)
filter_tensor = np.random.rand(5, 5, 1, 1).astype(np.float32)

# Use tf.raw_ops.conv2d to compute the 2-D convolution
output = tf.raw_ops.Conv2D(input=tf.constant(input_tensor),
                           filter=tf.constant(filter_tensor),
                           padding='VALID',
                           strides=[1, 1, 1, 1],
                           dilations=[1, 1, 1, 1],
                           data_format='NHWC',
                           name='conv2d')

# Print the shape of the output tensor
print(output.shape)
