import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[0, 1, 0], [2, 0, 3]], dtype=tf.int32)

# Apply the sparse-output bin counting function
binoting_sum = tf.raw_ops.BinCount(input_tensor, num_codePoints=2)

# Print the output
print(binoting_sum)
