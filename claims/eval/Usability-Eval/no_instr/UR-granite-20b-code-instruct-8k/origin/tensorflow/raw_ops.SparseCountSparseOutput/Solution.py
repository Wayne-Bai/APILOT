
import tensorflow as tf

# Define input sparse tensor
indices = tf.constant([[0, 0], [1, 1], [2, 3]])
values = tf.constant([1, 2, 3])
dense_shape = tf.constant([3, 4])
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Perform sparse-output bin counting
weights = tf.constant([0.5, 0.5, 0.5, 0.5])
bincount = tf.raw_ops.SparseBinCount(
    sparse_indices=sparse_tensor.indices,
    sparse_values=sparse_tensor.values,
    sparse_shape=sparse_tensor.dense_shape,
    weights=weights,
    minlength=0,
    maxlength=4,
    dtype=tf.int32
)

# Print the result
with tf.Session() as sess:
    print(sess.run(bincount))
