import tensorflow as tf

def compute_2d_convolution(input_tensor, filter_tensor, strides=(1, 1), padding='VALID'):
    """
    Computes a 2-D convolution given 4-D input and filter tensors.
    
    Args:
        input_tensor (tf.Tensor): A 4-D tensor of shape [batch, height, width, in_channels].
        filter_tensor (tf.Tensor): A 4-D tensor of shape [filter_height, filter_width, in_channels, out_channels].
        strides (tuple): A tuple of 2 integers, specifying the stride of the sliding window for each dimension of the input tensor.
        padding (str): One of "VALID" or "SAME". The type of padding algorithm to use.

    Returns:
        tf.Tensor: The result of the convolution operation.
    """
    # Performing the 2D convolution
    output_tensor = tf.nn.conv2d(
        input=input_tensor,
        filters=filter_tensor,
        strides=strides,
        padding=padding
    )
    
    return output_tensor
