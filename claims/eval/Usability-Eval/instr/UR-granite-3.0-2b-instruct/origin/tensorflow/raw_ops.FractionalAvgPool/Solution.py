import tensorflow as tf

# Define the fractional average pooling operation
def fractional_avg_pool(input_tensor, pool_size, strides, dilations, name=None):
    """
    Performs fractional average pooling on the input.

    Args:
        input_tensor (tf.Tensor): The input tensor to pool.
        pool_size (tf.Tensor): The pool size.
        strides (tf.Tensor): The strides.
        dilations (tf.Tensor): The dilations.
        name (str, optional): The name of the operation.

    Returns:
        tf.Tensor: The pooled tensor.
    """
    # Create a fractional average pooling operation
    op = tf.raw_ops.FractionalAvgPool(
        input=input_tensor,
        pool_size=pool_size,
        strides=strides,
        dilations=dilations,
        name=name
    )

    # Return the pooled tensor
    return op
