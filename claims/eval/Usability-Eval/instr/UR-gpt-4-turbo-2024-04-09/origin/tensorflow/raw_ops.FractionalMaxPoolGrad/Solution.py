import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=True):
    """
    Compute gradient of the Fractional Max Pool function.
    
    Args:
        orig_input (tf.Tensor): Original input to `fractional_max_pool`.
        orig_output (tf.Tensor): Original output from `fractional_max_pool`.
        out_backprop (tf.Tensor): Backpropagated gradients to `fractional_max_pool`.
        row_pooling_sequence (tf.Tensor): Row pooling sequence used for the pooling.
        col_pooling_sequence (tf.Tensor): Column pooling sequence used for the pooling.
        overlapping (bool): Whether the pooling is overlapping.
    
    Returns:
        tf.Tensor: Gradients w.r.t the input to `fractional_max_pool`.
    """
    return tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        out_backprop=out_backprop,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence,
        overlapping=overlapping
    )

# Example usage:
# Assuming `x`, `output`, `grads`, `row_seq`, `col_seq` setup correctly:
# gradients = fractional_max_pool_grad(x, output, grads, row_seq, col_seq)
