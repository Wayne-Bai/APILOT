
import tensorflow as tf

@tf.function
def compute_convolution_input_gradient(input_shape, filter, output_gradient):
    return tf.nn.conv2d_backprop_input(input_shape, filter, output_gradient, strides=[1, 1, 1, 1], padding='SAME')

# Example Usage
input_shape = [1, 5, 5, 3]  # [batch, height, width, channels]
filter = tf.random.normal([3, 3, 3, 2])  # [filter_height, filter_width, in_channels, out_channels]
output_gradient = tf.random.normal([1, 5, 5, 2])  # [batch, height, width, out_channels]

input_gradient = compute_convolution_input_gradient(input_shape, filter, output_gradient)
print(input_gradient)
