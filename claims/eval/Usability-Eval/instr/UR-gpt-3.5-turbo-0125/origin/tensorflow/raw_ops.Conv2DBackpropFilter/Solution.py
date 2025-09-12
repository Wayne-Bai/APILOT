
import tensorflow as tf

# Define a custom function to compute gradients of convolution with respect to the filter
@tf.function
def conv2d_filter_gradients(input, filter, strides, padding, input_backprop):
    grad_filter = tf.nn.conv2d_backprop_filter(input, filter, input_backprop, strides=strides, padding=padding)
    return grad_filter
