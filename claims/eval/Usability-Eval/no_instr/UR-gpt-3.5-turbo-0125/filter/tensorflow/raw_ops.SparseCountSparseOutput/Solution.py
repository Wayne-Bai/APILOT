
import tensorflow as tf

# Define sparse tensor input
values = tf.constant([1, 3, 1, 4, 2, 4])
indices = tf.constant([[0, 0], [0, 2], [1, 1], [1, 2], [2, 0], [2, 2]])
dense_shape = tf.constant([3, 4])

sparse_input = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define method to perform sparse-output bin counting for the sparse tensor input
output = tf.raw_ops.SparseBincount(sparse_indices=sparse_input.indices, minlength=5)

print(output)
