import tensorflow as tf

def conv2d(input_tensor, filter_tensor, strides, padding):
    return tf.nn.conv2d(input_tensor, filter_tensor, strides=strides, padding=padding)

# Example usage:
# input_tensor = tf.random.normal([1, 28, 28, 3])  # [batch, height, width, channels]
# filter_tensor = tf.random.normal([5, 5, 3, 16])  # [filter_height, filter_width, in_channels, out_channels]
# strides = [1, 1, 1, 1]
# padding = 'SAME'
# result = conv2d(input_tensor, filter_tensor, strides, padding)
