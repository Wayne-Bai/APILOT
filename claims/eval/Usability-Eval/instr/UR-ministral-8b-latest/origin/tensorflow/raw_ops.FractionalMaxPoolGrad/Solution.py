import tensorflow as tf

def fractional_max_pool(input_tensor, ksize=(2, 2), strides=(2, 2), padding='VALID', data_format='_default'):
    """
    Compute the fractional max pooling of the input tensor.

    Args:
        input_tensor (tf.Tensor): The input tensor to perform max pooling on.
        ksize (tuple): The size of the window for each dimension.
        strides (tuple): The stride of the sliding window.
        padding (str): The type of padding algorithm. Padding defaults to 'VALID'.
        data_format (str): The data format through which to pass the data. 'Default' means channels last (N, H, W, C), 'NHWC' means channels last, 'NCHW' means channels first.

    Returns:
        tf.Tensor: A tensor of the same shape as input_tensor with max pooled values.
    """
    # Fractional Max Pooling implementation
    max_pool = tf.nn.max_pool2d(input=input_tensor,
                                ksize=[ksize[1], ksize[0], 1, 1],
                                strides=strides,
                                padding=padding,
                                data_format='NHWC' if data_format == 'c' else 'NCHW')

    return max_pool

# Test the function
input_tensor = tf.constant([[[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]])
result = fractional_max_pool(input_tensor)
print(result)
