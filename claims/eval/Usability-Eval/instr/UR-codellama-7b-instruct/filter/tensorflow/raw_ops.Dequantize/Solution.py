
import tensorflow as tf

# Define the input tensor
input = tf.constant([1, 2, 3, 4, 5], shape=[5])

# Dequantize the input tensor
output = tf.raw_ops.Dequantize(input=input, min_range=0, max_range=256)

print(output)
