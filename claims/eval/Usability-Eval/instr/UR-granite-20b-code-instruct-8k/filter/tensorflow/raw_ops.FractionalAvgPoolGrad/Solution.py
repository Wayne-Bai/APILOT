import tensorflow as tf

def fractional_avg_pool_grad(input, out_backprop, pool_size, strides, padding):
    """
    Computes the gradient of the FractionalAvgPool function.
    
    Args:
        input: A 4-D Tensor of type float and shape [batch, height, width, channels].
        out_backprop: A 4-D Tensor of type float and shape [batch, height, width, channels].
        pool_size: A list of integers [pool_height, pool_width] specifying the size of the pooling window.
        strides: A list of integers [stride_height, stride_width] specifying the stride of the pooling window.
        padding: A string, either 'VALID' or 'SAME', specifying the padding algorithm.
    
    Returns:
        A 4-D Tensor of type float and shape [batch, height, width, channels].
    """
    return tf.raw_ops.FractionalAvgPoolGrad(
        orig_input_tensor_shape=tf.shape(input),
        out_backprop=out_backprop,
        pool_size=pool_size,
        strides=strides,
        padding=padding
    )
