import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    """
    Computes the gradient of the FractionalMaxPool function.

    Args:
        orig_input: The original input tensor.
        orig_output: The original output tensor from FractionalMaxPool.
        out_backprop: The backpropagated gradient tensor.
        row_pooling_sequence: The row pooling sequence.
        col_pooling_sequence: The column pooling sequence.
        overlapping: Whether to allow overlapping regions in pooling.

    Returns:
        The gradient tensor.
    """
    # Create a mask to identify the maximum values in the original output
    mask = tf.equal(orig_output, orig_input)

    # Expand dimensions to match the shape of out_backprop
    mask = tf.expand_dims(mask, axis=-1)

    # Tile the mask to match the shape of out_backprop
    mask = tf.tile(mask, [1, 1, 1, tf.shape(out_backprop)[-1]])

    # Apply the mask to the backpropagated gradient
    grad = tf.where(mask, out_backprop, tf.zeros_like(out_backprop))

    # Sum the gradients over the pooling regions
    grad = tf.reduce_sum(grad, axis=[1, 2], keepdims=True)

    return grad

# Example usage:
# orig_input = ...
# orig_output = ...
# out_backprop = ...
# row_pooling_sequence = ...
# col_pooling_sequence = ...
# gradient = fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence)
