import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([1, 16, 16, 3])

# Define the pool size and the ratio of input to output pooling window size
pool_size = [14, 14]
pool_ratio = 1.0

# Perform fractional average pooling
output_tensor = tf.raw_ops.FractionalAvgPool(input_tensor, pool_size, pool_ratio)

# Print the output tensor shape
print(output_tensor.shape)
