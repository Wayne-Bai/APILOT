import tensorflow as tf

def fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    # Compute the gradient of the FractionalAvgPool function
    grad = tf.raw_ops.FractionalAvgPoolGrad(
        orig_input_tensor_shape=orig_input_tensor_shape,
        out_backprop=out_backprop,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence,
        overlapping=overlapping
    )
    return grad

# Example usage:
# orig_input_tensor_shape = [batch, height, width, channels]
# out_backprop = gradient from the next layer
# row_pooling_sequence = [0, pooled_height1, pooled_height2, ..., height]
# col_pooling_sequence = [0, pooled_width1, pooled_width2, ..., width]
# overlapping = False (or True if overlapping pooling is used)

# Example values
orig_input_tensor_shape = [1, 6, 6, 1]
out_backprop = tf.random.normal([1, 3, 3, 1])
row_pooling_sequence = [0, 2, 4, 6]
col_pooling_sequence = [0, 2, 4, 6]
overlapping = False

grad = fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping)
print(grad)
