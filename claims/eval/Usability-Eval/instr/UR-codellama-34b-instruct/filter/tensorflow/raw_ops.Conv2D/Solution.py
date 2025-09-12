
import tensorflow as tf

# Define the input tensor
input_tensor = tf.random_normal(shape=(10, 10, 3))

# Define the filter tensor
filter_tensor = tf.random_normal(shape=(3, 3, 3, 64))

# Perform a 2D convolution using the `tf.raw_ops.Conv2d` op
output_tensor = tf.raw_ops.Conv2d(input_tensor, filter_tensor)

print("Output shape:", output_tensor.shape)
