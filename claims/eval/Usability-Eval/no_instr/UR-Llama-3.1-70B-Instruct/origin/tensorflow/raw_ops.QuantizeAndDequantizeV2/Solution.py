# Importing the necessary libraries
import tensorflow as tf

# Create a tensor
tensor = tf.constant([-1.5, -0.5, 0.5, 1.5], dtype=tf.float32)

# Quantizes then dequantizes a tensor
output = tf.raw_ops.Dequantize(tensor, min_range=-1.0, max_range=1.0, mode="SCALED", signed_input=True, range_given=True, narrow_range=False, dtype=tf.float32)

# Convert the output to float32 (by default output will be float32)
output = tf.cast(output, tf.float32)

# Print the output
print("Input tensor:", tensor)
print("Output tensor after dequantization:", output)
