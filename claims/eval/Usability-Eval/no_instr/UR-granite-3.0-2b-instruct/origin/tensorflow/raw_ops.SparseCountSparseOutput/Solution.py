import tensorflow as tf

# Define the sparse tensor input
sparse_input = tf.constant([[0, 0, 1], [2, 0, 0], [0, 3, 0]])

# Define the bin count
bin_count = 2

# Perform sparse-output bin counting
sparse_bin_count = tf.raw_ops.SparseBinCount(sparse_input, bin_count)

# Print the result
print(sparse_bin_count)
