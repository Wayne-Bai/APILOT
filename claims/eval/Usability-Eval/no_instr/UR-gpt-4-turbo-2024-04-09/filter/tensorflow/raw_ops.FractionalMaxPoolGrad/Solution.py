import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, output_gradient, row_pooling_sequence, col_pooling_sequence):
    # Compute the gradients for fractional max pooling
    return tf.raw_ops.FractionalMaxPoolGrad(orig_input=orig_input,
                                            orig_output=orig_output,
                                            out_backprop=output_gradient,
                                            row_pooling_sequence=row_pooling_sequence,
                                            col_pooling_sequence=col_pooling_sequence,
                                            overlapping=True)

# Example usage:
# Assuming `orig_input`, `orig_output`, `output_gradient`, `row_pooling_sequence`, and `col_pooling_sequence`
# are defined appropriately. They should have been obtained during the forward pass.
# This is a placeholder for tensors that would be obtained in a complete example.
# orig_input = tf.random.normal([1, 10, 10, 1])
# orig_output, row_pooling_sequence, col_pooling_sequence = tf.raw_ops.FractionalMaxPool(...)
# output_gradient = tf.random.normal(orig_output.shape)

# grad = fractional_max_pool_grad(orig_input, orig_output, output_gradient, row_pooling_sequence, col_pooling_sequence)
