import tensorflow as tf

def fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    # Compute the gradient for FractionalAvgPool
    grad = tf.zeros(orig_input_tensor_shape, dtype=out_backprop.dtype)
    
    # Iterate over the pooling sequences to distribute the gradient
    for i, (rstart, rend) in enumerate(zip(row_pooling_sequence[:-1], row_pooling_sequence[1:])):
        for j, (cstart, cend) in enumerate(zip(col_pooling_sequence[:-1], col_pooling_sequence[1:])):
            if overlapping:
                grad[rstart:rend, cstart:cend] += out_backprop[i, j]
            else:
                grad[rstart:rend, cstart:cend] = out_backprop[i, j]
    
    return grad

# Example usage:
# orig_input_tensor_shape = [4, 4]
# out_backprop = tf.constant([[1.0, 2.0], [3.0, 4.0]])
# row_pooling_sequence = [0, 2, 4]
# col_pooling_sequence = [0, 2, 4]
# overlapping = False
# result = fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping)
# print(result)
