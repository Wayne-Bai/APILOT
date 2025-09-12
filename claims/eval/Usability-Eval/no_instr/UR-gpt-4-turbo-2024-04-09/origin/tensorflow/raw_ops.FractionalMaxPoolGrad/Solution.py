import tensorflow as tf

# Assume 'orig_input' is the original input tensor to the FractionalMaxPool operation
# and 'orig_output' is the output tensor obtained from the FractionalMaxPool operation.
# 'row_pooling_sequence' and 'col_pooling_sequence' are the pooling sequence for the row and column.
# These tensors should be captured during the FractionalMaxPool operation.

# Sample shapes and values for demonstration purposes
orig_input = tf.random.normal([1, 10, 10, 3])  # Shape: [batch, height, width, channels]
orig_output, row_pooling_sequence, col_pooling_sequence = tf.raw_ops.FractionalMaxPool(
    value=orig_input,
    pooling_ratio=[1.0, 1.44, 1.44, 1.0],
    pseudo_random=True,
    overlapping=True
)

# Gradient computation
out_backprop = tf.ones_like(orig_output)  # Dummy gradient w.r.t output
grad = tf.raw_ops.FractionalMaxPoolGrad(
    orig_input=orig_input,
    orig_output=orig_output,
    out_backprop=out_backprop,
    row_pooling_sequence=row_pooling_sequence,
    col_pooling_sequence=col_pooling_sequence,
    overlapping=True
)

# Print the gradient tensor
print("Gradients w.r.t input:", grad)
