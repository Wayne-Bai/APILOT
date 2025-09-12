import tensorflow as tf

# Define the input tensor
input_tensor = tf.random.normal([1, 10, 10, 10])

# Define the pooling parameters
pooling_ratio = [1.0, 1.0]

# Perform fractional average pooling
output_tensor = tf.raw_ops.FractionalAvgPool(input_tensor, pooling_ratio,
                                               overlapping=True,
                                               deterministic=True)

# Print the output tensor
print(output_tensor)
