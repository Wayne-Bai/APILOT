import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    # Compute the gradient of the FractionalMaxPool function
    grad = tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        out_backprop=out_backprop,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence,
        overlapping=overlapping
    )
    return grad

# Example usage:
# orig_input = ...
# orig_output = ...
# out_backprop = ...
# row_pooling_sequence = ...
# col_pooling_sequence = ...
# grad = fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence)
