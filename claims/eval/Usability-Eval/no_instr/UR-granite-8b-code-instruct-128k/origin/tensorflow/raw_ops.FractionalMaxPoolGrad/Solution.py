import tensorflow as tf

# Create input tensors
orig_input = tf.random.normal([1, 2, 3, 4])
orig_output = tf.nn.fractional_max_pool(orig_input, [1, 1, 2, 2], [1, 1, 2, 2], padding='SAME')
out_backprop = tf.random.normal([1, 1, 2, 2])

# Call the FractionalMaxPoolGrad function
grad = tf.raw_ops.FractionalMaxPoolGrad(
    orig_input=orig_input,
    orig_output=orig_output,
    out_backprop=out_backprop,
    pseudo_random=False,
    overlapping=False,
    deterministic=False,
    seed=0,
    seed2=0
)

# Print the result
print(grad)
