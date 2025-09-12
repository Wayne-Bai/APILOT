import tensorflow as tf

# Define the input sparse tensor
sparse_input = tf.SparseTensor(
    indices=[[0, 0], [1, 2], [2, 3]],
    values=[1, 2, 3],
    dense_shape=[3, 4]
)

# Perform sparse-output bin counting
sparse_output = tf.raw_ops.SparseBincount(
    sparse_input,
    num_bins=5,
    range_start=0,
    range_limit=10
)

# Print the sparse output
print(sparse_output)
