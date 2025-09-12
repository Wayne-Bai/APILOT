import tensorflow as tf

# Define the forward FractionalAvgPool operation
def fractional_avg_pool(x):
    pool_size = (1.5, 1.5)  # Example pool size
    return tf.raw_ops.FractionalAvgPool(
        value=x,
        pooling_ratio=[1.0, *pool_size, 1.0],
        pseudo_random=False,
        overlapping=False,
        deterministic=False,
        seed=0,
        seed2=0
    )

# Create a random tensor
input_tensor = tf.random.uniform(shape=[1, 10, 10, 1], minval=0, maxval=1)

# Compute the forward operation
with tf.GradientTape() as tape:
    tape.watch(input_tensor)
    pooled_output, row_seq, col_seq = fractional_avg_pool(input_tensor)

# Compute the gradient of the FractionalAvgPool operation
gradient = tape.gradient(pooled_output, input_tensor)

print("Pooled Output:\n", pooled_output)
print("Gradient:\n", gradient)
