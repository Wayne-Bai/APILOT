import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, grad, row_pooling_sequence, col_pooling_sequence, overlapping=False):
    # Compute the gradient of the FractionalMaxPool function
    grad_shape = tf.shape(grad)
    orig_input_shape = tf.shape(orig_input)
    
    # Initialize the gradient for the input
    input_grad = tf.zeros_like(orig_input)
    
    # Iterate over the pooling sequences
    for i in range(grad_shape[0]):
        for j in range(grad_shape[1]):
            # Get the pooling region indices
            row_start = row_pooling_sequence[i]
            row_end = row_pooling_sequence[i + 1]
            col_start = col_pooling_sequence[j]
            col_end = col_pooling_sequence[j + 1]
            
            # Extract the pooling region from the original input
            pooling_region = orig_input[row_start:row_end, col_start:col_end]
            
            # Find the indices of the maximum values in the pooling region
            max_indices = tf.where(tf.equal(pooling_region, orig_output[i, j]))
            
            # Distribute the gradient to the maximum values
            for idx in max_indices:
                input_grad = tf.tensor_scatter_nd_add(input_grad, [[row_start + idx[0], col_start + idx[1]]], [grad[i, j]])
    
    return input_grad

# Example usage
orig_input = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
orig_output = tf.constant([[5.0, 6.0], [8.0, 9.0]])
grad = tf.constant([[1.0, 2.0], [3.0, 4.0]])
row_pooling_sequence = [0, 1, 3]
col_pooling_sequence = [0, 2, 3]

result = fractional_max_pool_grad(orig_input, orig_output, grad, row_pooling_sequence, col_pooling_sequence)
print(result.numpy())
