import tensorflow as tf

# Create a sparse tensor input
sparse_input = tf.sparse.from_dense(tf.constant([[0, 0, 0], [1, 0, 0], [0, 2, 0]]))

# Perform sparse-output bin counting
result = tf.raw_ops.SparseBinCount(sparse_input, num_bins=3)

# Print the result
print(result)
