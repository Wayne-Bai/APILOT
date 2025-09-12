import tensorflow as tf

# Assuming you have a function `fractional_avg_pool` that wraps tf.raw_ops.FractionalAvgPool
def fractional_avg_pool(value, pooling_ratio, pseudo_random=None, overlapping=None, deterministic=None, seed=None, seed2=None):
    return tf.raw_ops.FractionalAvgPool(value=value,
                                        pooling_ratio=pooling_ratio,
                                        pseudo_random=pseudo_random,
                                        overlapping=overlapping,
                                        deterministic=deterministic,
                                        seed=seed,
                                        seed2=seed2)

# Creating a dummy input tensor
input_tensor = tf.random.normal(shape=[1, 4, 4, 1])

# Pooling ratio for the fractional pooling operation
pooling_ratio = [1.0, 1.4, 1.4, 1.0]

# Run the forwards pass
output, row_pooling_sequence, col_pooling_sequence = fractional_avg_pool(input_tensor, pooling_ratio)

# Create a gradient function
def gradient_fractional_avg_pool(orig_input, grad):
    return tf.raw_ops.FractionalAvgPoolGrad(orig_input=orig_input,
                                            out_backprop=grad,
                                            row_pooling_sequence=row_pooling_sequence,
                                            col_pooling_sequence=col_pooling_sequence)

# Create a gradient for the output
grad_output = tf.ones_like(output)

# Compute the gradients
input_grads = gradient_fractional_avg_pool(input_tensor, grad_output)
print("Input gradients:\n", input_grads)
