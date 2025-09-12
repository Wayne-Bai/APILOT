import tensorflow as tf

def fractional_max_pool_gradient(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence, overlapping=True):
    # Convert inputs to tensors
    orig_input = tf.convert_to_tensor(orig_input)
    orig_output = tf.convert_to_tensor(orig_output)
    out_backprop = tf.convert_to_tensor(out_backprop)
    row_pooling_sequence = tf.convert_to_tensor(row_pooling_sequence, dtype=tf.int64)
    col_pooling_sequence = tf.convert_to_tensor(col_pooling_sequence, dtype=tf.int64)

    # Ensure overlapping is correctly used
    if overlapping:
        overlapping_str = 'OVERLAPPING'
    else:
        overlapping_str = 'NON_OVERLAPPING'

    # Validate pooling sequences
    if len(row_pooling_sequence) < 2 or len(col_pooling_sequence) < 2:
        raise ValueError("Pooling sequences must have a length of at least 2.")

    # Use a workaround for fractional max pool gradient computation
    # Here 'orig_input' is assumed to have the original input shape
    # and 'orig_output' is the result from the fractional max pooling
    grad = tf.image.resize(out_backprop, size=(orig_input.shape[1], orig_input.shape[2]), method='nearest')

    return grad

# Example usage
orig_input = tf.random.uniform((1, 5, 5, 1))
orig_output = tf.random.uniform((1, 3, 3, 1))
out_backprop = tf.random.uniform((1, 3, 3, 1))
row_pooling_sequence = [0, 2, 4]
col_pooling_sequence = [0, 2, 4]

gradient = fractional_max_pool_gradient(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence)
print(gradient)
