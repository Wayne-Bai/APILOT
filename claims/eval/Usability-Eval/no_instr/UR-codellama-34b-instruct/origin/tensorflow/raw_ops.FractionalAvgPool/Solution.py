
import tensorflow as tf

# Define the input data and parameters for the pooling operation
input_data = tf.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
pool_size = (2, 2)
strides = (1, 1)
padding = 'SAME'

# Perform the pooling operation using tf.nn.fractional_avg_pool
output = tf.nn.fractional_avg_pool(input_data, pool_size, strides, padding)

# Print the output
print(output)
