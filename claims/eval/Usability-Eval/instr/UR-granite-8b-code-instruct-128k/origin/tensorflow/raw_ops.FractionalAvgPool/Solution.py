import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal((1, 8, 8, 3))

# Define the fractional average pooling operation
output_tensor = tf.raw_ops.FractionalAvgPool(
    value=input_tensor,
    pooling_ratio=[1.0, 1.0, 1.0, 1.0],
    pseudo_random=False,
    overlapping=False,
    deterministic=False,
    seed=0,
    seed2=0
)

# Print the output tensor
print(output_tensor)
