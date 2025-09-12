import tensorflow as tf

def fractional_max_pool(x, pooling_ratio, padding, data_format):
    """Computes gradient of the FractionalMaxPool function.
    
    Args:
      x: A `Tensor` with shape [batch, in_height, in_width, in_channels].
      pooling_ratio: An int or tuple/list of two ints, specifying the pooling size. Can be a single int to specify the same value for all dimensions.
      padding: A string, either 'SAME' or 'VALID'. The padding algorithm.
      data_format: A string, one of "NHWC" (default) or "NCHW". The ordering of the dimensions in the input.
    
    Returns:
      A `Tensor` with shape [batch, out_height, out_width, in_channels].
    """
    return tf.nn.fractional_max_pool(x, pooling_ratio=pooling_ratio, padding=padding, data_format=data_format)
