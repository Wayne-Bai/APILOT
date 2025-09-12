import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_seq, col_seq, overlapping):
    # Compute shapes
    orig_input_shape = tf.shape(orig_input, out_type=tf.int64)
    orig_output_shape = tf.shape(orig_output, out_type=tf.int64)
    out_backprop_shape = tf.shape(out_backprop, out_type=tf.int64)

    # Log the shapes for debugging
    tf.print("Original input shape:", orig_input_shape)
    tf.print("Original output shape:", orig_output_shape)
    tf.print("Out backprop shape:", out_backprop_shape)

    # Use tf.raw_ops.FractionalMaxPoolGrad with necessary input values
    grad = tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        out_backprop=out_backprop,
        row_pooling_sequence=row_seq,
        col_pooling_sequence=col_seq,
        overlapping=overlapping
    )

    return grad

# Example usage:
# Assume `orig_input`, `orig_output`, `out_backprop` are your tensors from the forward pass.
orig_input = tf.random.uniform([1, 28, 28, 1])
orig_output = tf.random.uniform([1, 14, 14, 1])
out_backprop = tf.random.uniform([1, 14, 14, 1])
row_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
col_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlapping = True

grad = fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_seq, col_seq, overlapping)
tf.print("Gradient:", grad)
