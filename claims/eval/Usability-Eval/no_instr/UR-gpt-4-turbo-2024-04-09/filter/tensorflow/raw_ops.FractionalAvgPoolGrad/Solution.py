import tensorflow as tf

def fractional_avg_pool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence):
    return tf.raw_ops.FractionalAvgPoolGrad(
        orig_input_shape=orig_input_tensor_shape,
        out_backprop=out_backprop,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence
    )

# Sample shapes and pooling sequence for demonstration
input_tensor_shape = [1, 6, 6, 1]   # Example input shape
output_grads = tf.random.normal([1, 3, 3, 1])  # Example gradients
row_seq = [0, 2, 4, 6]  # Example row pooling sequence
col_seq = [0, 3, 6]    # Example column pooling sequence

# Compute the gradient of FractionalAvgPool
grads = fractional_avg_pool_grad(input_tensor_shape, output_grads, row_seq, col_seq)
print(grads)
