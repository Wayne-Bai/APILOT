import tensorflow as tf

# Create a sample input tensor with shape [batch_size, height, width, channels]
input_tensor = tf.random.uniform(shape=[1, 4, 4, 1], minval=0, maxval=1)

# Define the parameters for the fractional max pooling
pooling_ratio = [1.0, 1.5, 1.5, 1.0]

# Perform fractional average pooling
fractional_avg_pool_output, row_pooling_sequence, col_pooling_sequence = tf.raw_ops.FractionalAvgPool(
    value=input_tensor,
    pooling_ratio=pooling_ratio,
    pseudo_random=False,
    overlapping=False,
    deterministic=False,
    seed=0,
    seed2=0
)

# Start a session and evaluate the output
print("Input Tensor:")
print(input_tensor.numpy())

print("\nFractional Average Pooling Output:")
print(fractional_avg_pool_output.numpy())

print("\nRow Pooling Sequence:")
print(row_pooling_sequence.numpy())

print("\nColumn Pooling Sequence:")
print(col_pooling_sequence.numpy())
