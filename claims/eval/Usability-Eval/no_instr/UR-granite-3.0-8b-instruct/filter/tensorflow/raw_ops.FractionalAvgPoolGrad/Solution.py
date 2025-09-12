import tensorflow as tf

def fractional_avg_pool_grad(input, pool_size, pooling_type, layout='NHWC'):
    """
    Computes gradient of the FractionalAvgPool function.

    Args:
    input: A 4-D input tensor.
    pool_size: A 1-D tensor representing the pool size.
    pooling_type: A string specifying the type of pooling, either 'AVG' or 'MAX'.
    layout: A string specifying the data layout, either 'NHWC' or 'NCHW'.

    Returns:
    A 4-D tensor representing the gradient of the FractionalAvgPool function.
    """
    # Compute the output tensor
    output = tf.raw_ops.FractionalAvgPool(input, pool_size, pooling_type, layout)

    # Compute the gradient tensor
    grad = tf.raw_ops.FractionalAvgPoolGrad(input, output, pool_size, pooling_type, layout)

    return grad
