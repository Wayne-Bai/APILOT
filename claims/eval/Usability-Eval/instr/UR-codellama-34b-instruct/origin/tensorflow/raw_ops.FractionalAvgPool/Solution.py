
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]])

# Define the pool size and strides
pool_size = [2, 2]
strides = [2, 2]

# Perform fractional average pooling on the input tensor
pooled_tensor = tf.nn.fractional_avg_pool(input_tensor, pool_size, strides)

print(pooled_tensor) # [[1, 1], [3, 3]]
