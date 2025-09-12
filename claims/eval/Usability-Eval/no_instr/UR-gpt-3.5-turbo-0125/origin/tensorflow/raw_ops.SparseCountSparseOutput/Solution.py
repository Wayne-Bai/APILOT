
import tensorflow as tf

# Define input sparse tensor
indices = tf.constant([[0, 0], [0, 2], [1, 1], [1, 3], [2, 1]])
values = tf.constant([1, 1, 1, 1, 1])
dense_shape = [3, 4]

sparse_input = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Use tf.raw_ops.sparse_bincount to perform sparse-counting
sparse_counts = tf.raw_ops.SparseBincount(sparse_indices=sparse_input.indices, minlength=5)

print(sparse_counts)
