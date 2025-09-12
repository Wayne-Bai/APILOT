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
# out_backprop = gradient of the output from FractionalAvgPool
# row_pooling_sequence = sequence of row indices from FractionalAvgPool
# col_pooling_sequence = sequence of column indices from FractionalAvgPool
# overlapping = whether pooling regions overlap

# Example values
orig_input_tensor_shape = [1, 10, 10, 3]
out_backprop = tf.random.normal([1, 5, 5, 3])
row_pooling_sequence = [0, 2, 4, 6, 8, 10]
col_pooling_sequence = [0, 2, 4, 6, 8, 10]

grad = fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence)
print(grad)
