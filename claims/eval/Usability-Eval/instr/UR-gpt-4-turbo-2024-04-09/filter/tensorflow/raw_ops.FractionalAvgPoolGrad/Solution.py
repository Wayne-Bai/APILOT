import tensorflow as tf

def fractional_avg_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence):
    return tf.raw_ops.FractionalAvgPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        out_backprop=out_backprop,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence
    )

# Example usage:
# Define the input tensor, outputs, gradients, and pooling sequences
input_tensor = tf.constant([[1., 2., 3., 4.],
                            [5., 6., 7., 8.],
                            [9., 10., 11., 12.],
                            [13., 14., 15., 16.]])

input_tensor = tf.reshape(input_tensor, [1, 4, 4, 1])
output, row_seq, col_seq = tf.raw_ops.FractionalAvgPool(
    value=input_tensor,
    pooling_ratio=[1.0, 1.44, 1.44, 1.0],
    pseudo_random=False,
    overlapping=True)

out_backprop = tf.ones_like(output)

# Compute the gradient
grads = fractional_avg_pool_grad(
    orig_input=input_tensor,
    orig_output=output,
    out_backprop=out_backprop,
    row_pooling_sequence=row_seq,
    col_pooling_sequence=col_seq
)

print("Gradients:\n", grads.numpy())
