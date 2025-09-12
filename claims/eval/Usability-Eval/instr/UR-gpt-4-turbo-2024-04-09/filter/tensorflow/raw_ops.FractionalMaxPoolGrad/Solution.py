import tensorflow as tf

def fractional_max_pool_grad(orig_input, orig_output, out_backprop, row_pooling_sequence, col_pooling_sequence):
    # Use tf.raw_ops.FractionalMaxPoolGrad to compute the gradient of the FractionalMaxPool
    return tf.raw_ops.FractionalMaxPoolGrad(
        orig_input=orig_input,
        orig_output=orig_output,
        out_backprop=out_backprop,
        row_pooling_sequence=row_pooling_sequence,
        col_pooling_sequence=col_pooling_sequence
    )

# Example to demonstrate the usage
input_tensor = tf.random.normal([1, 8, 8, 1])
pooling_ratio = [1.0, 1.44, 1.73, 1.0]

# Performing fractional max pooling
output, row_seq, col_seq = tf.raw_ops.FractionalMaxPool(value=input_tensor, pooling_ratio=pooling_ratio, pseudo_random=True)

# Simulate a gradient coming from the next layer
grad_tensor = tf.random.normal(output.shape)

# Compute the gradients using the defined function
gradient_input = fractional_max_pool_grad(orig_input=input_tensor, orig_output=output, out_backprop=grad_tensor, row_pooling_sequence=row_seq, col_pooling_sequence=col_seq)

print("Gradient w.r.t the input:", gradient_input)
