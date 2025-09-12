import tensorflow as tf

# Create a tensor of integers
inputs = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)

# Use the tf.raw_ops.EncodeWav function to encode the integers into a tensor of Unicode strings
output = tf.raw_ops.EncodeWav(audio=inputs)

# Print the output tensor
print(output)
