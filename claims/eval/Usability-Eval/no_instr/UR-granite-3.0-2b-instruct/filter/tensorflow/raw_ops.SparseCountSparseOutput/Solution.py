import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[0, 0, 0], [1, 0, 0], [0, 2, 0], [0, 0, 3]])

# Define the bin counts
bin_counts = tf.constant([[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]])

# Perform sparse-output bin counting
result = tf.raw_ops.SparseBinCount(input_tensor, bin_counts)

# Print the result
print(result)
