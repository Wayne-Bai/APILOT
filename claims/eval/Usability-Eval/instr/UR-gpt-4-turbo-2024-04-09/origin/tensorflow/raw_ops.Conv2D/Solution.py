import tensorflow as tf

def compute_2d_convolution(input_tensor, filter_tensor, strides, padding):
    """
    Computes a 2-D convolution using the given input and filter tensors.
    
    Args:
    input_tensor (tf.Tensor): A 4-D tensor with shape [batch, in_height, in_width, in_channels].
    filter_tensor (tf.Tensor): A 4-D tensor with shape [filter_height, filter_width, in_channels, out_channels].
    strides (list of ints): The stride of the sliding window for each dimension of input.
    padding (str): Either "SAME" or "VALID" indicating the type of padding algorithm to use.

    Returns:
    tf.Tensor: The result of the convolution, a 4-D tensor.
    """
    return tf.nn.conv2d(input=input_tensor, filters=filter_tensor, strides=strides, padding=padding)

# Example usage
input_tensor = tf.random.normal([1, 10, 10, 3])  # Example input: batch of 1, 10x10 image, 3 channels
filter_tensor = tf.random.normal([3, 3, 3, 8])   # Example filter: 3x3 size, 3 input channels, 8 output channels
strides = [1, 1, 1, 1]
padding = 'SAME'

output_tensor = compute_2d_convolution(input_tensor, filter_tensor, strides, padding)
print(output_tensor)
