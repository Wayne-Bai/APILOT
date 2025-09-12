import tensorflow as tf

def compute_fractional_avgpool_grad(orig_input_tensor_shape, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    """
    Computes the gradient of the FractionalAvgPool function.
    
    Parameters:
        orig_input_tensor_shape (tuple): The shape of the original input tensor.
        out_backprop (tf.Tensor): Backpropagated gradients to the output.
        row_pooling_sequence (list): Sequence used for row pooling.
        col_pooling_sequence (list): Sequence used for column pooling.
        overlapping (bool): Whether pooling regions overlap.
    
    Returns:
        tf.Tensor: Gradient w.r.t the input of FractionalAvgPool.
    """
    
    # Convert sequences to tensors
    row_seq_tensor = tf.convert_to_tensor(row_pooling_sequence, dtype=tf.int64)
    col_seq_tensor = tf.convert_to_tensor(col_pooling_sequence, dtype=tf.int64)
    
    # Use tf.raw_ops.FractionalAvgPoolGrad
    pool_grad = tf.raw_ops.FractionalAvgPoolGrad(
        orig_input_tensor_shape=orig_input_tensor_shape,
        out_backprop=out_backprop,
        row_pooling_sequence=row_seq_tensor,
        col_pooling_sequence=col_seq_tensor,
        overlapping=overlapping
    )
    
    return pool_grad

# Example usage:
# Define original input tensor shape
input_shape = (1, 4, 4, 1)

# Simulate backpropagated gradients to the output
out_backprop = tf.random.normal((1, 3, 3, 1))

# Define row and column pooling sequence
row_pool_seq = [0, 1, 3, 4]
col_pool_seq = [0, 2, 4]

# Compute gradient
grad = compute_fractional_avgpool_grad(input_shape, out_backprop, row_pool_seq, col_pool_seq)
print(grad)
