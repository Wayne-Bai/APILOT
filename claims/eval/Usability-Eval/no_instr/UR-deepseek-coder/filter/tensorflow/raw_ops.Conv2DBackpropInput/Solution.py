import tensorflow as tf

def conv2d_grad_input(input_shape, filter, out_backprop, strides, padding, data_format='NHWC', dilations=[1, 1, 1, 1]):
    with tf.GradientTape() as tape:
        tape.watch(tf.zeros(input_shape))
        output = tf.nn.conv2d(tf.zeros(input_shape), filter, strides, padding, data_format=data_format, dilations=dilations)
    grad = tape.gradient(output, tf.zeros(input_shape), output_grad=out_backprop)
    return grad

# Example usage:
input_shape = [1, 5, 5, 3]  # [batch, height, width, channels]
filter = tf.random.normal([3, 3, 3, 16])  # [filter_height, filter_width, in_channels, out_channels]
out_backprop = tf.random.normal([1, 5, 5, 16])  # [batch, height, width, out_channels]
strides = [1, 1, 1, 1]
padding = 'SAME'

grad_input = conv2d_grad_input(input_shape, filter, out_backprop, strides, padding)
print(grad_input)
