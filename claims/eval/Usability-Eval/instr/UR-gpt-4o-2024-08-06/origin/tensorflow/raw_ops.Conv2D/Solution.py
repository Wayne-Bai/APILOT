import tensorflow as tf

# Define the 2-D convolution function
def conv2d(input_tensor, filter_tensor, strides, padding):
    """
    Performs a 2-D convolution given an input tensor and a filter tensor.

    :param input_tensor: 4-D tensor of shape [batch, in_height, in_width, in_channels]
    :param filter_tensor: 4-D tensor of shape [filter_height, filter_width, in_channels, out_channels]
    :param strides: A list of ints. The stride of the sliding window for each dimension of input. Must have length 4.
    :param padding: A string, either 'VALID' or 'SAME'. The type of padding algorithm to use.

    :return: Output tensor after applying the convolution
    """
    return tf.nn.conv2d(input=input_tensor, filters=filter_tensor, strides=strides, padding=padding)

# Example usage
# Example input: 1 batch, 5x5 image, 1 channel
input_tensor = tf.random.normal([1, 5, 5, 1])

# Example filter: 3x3 filter, 1 input channel, 1 output channel
filter_tensor = tf.random.normal([3, 3, 1, 1])

# Strides: Example with no stride (1), and padding type 'SAME'
strides = [1, 1, 1, 1]
padding = 'SAME'

# Perform the convolution
output_tensor = conv2d(input_tensor, filter_tensor, strides, padding)

print("Output tensor:", output_tensor)
