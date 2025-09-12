import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, grad, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    """
    Computes the gradient of FractionalMaxPool.

    Parameters:
    orig_input : The original input to `fractional_max_pool`.
    orig_output : The original output from `fractional_max_pool`.
    grad : Gradient from the output of `fractional_max_pool`.
    row_pooling_sequence : Row pool sequence used during pooling.
    col_pooling_sequence : Column pool sequence used during pooling.
    overlapping : Whether the pooling is overlapping.

    Returns:
    Gradient for the input of `fractional_max_pool`.
    """
    input_shape = tf.shape(orig_input)
    grad_shape = tf.shape(grad)
    
    # Compute gradient using FractionalMaxPoolGrad
    grad_input = tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        grad=grad,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence,
        overlapping=overlapping,
        name=None
    )
    
    return tf.reshape(grad_input, input_shape)
