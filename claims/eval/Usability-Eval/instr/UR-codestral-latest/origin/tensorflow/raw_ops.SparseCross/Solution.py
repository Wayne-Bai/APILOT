import tensorflow as tf

# Define your sparse and dense tensors
sparse_indices = tf.constant([[0, 0], [1, 2]], dtype=tf.int64)
sparse_values = tf.constant([1, 2], dtype=tf.float32)
sparse_shape = tf.constant([3, 4], dtype=tf.int64)

dense_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=tf.float32)

# Use tf.raw_ops.SparseCross to calculate sparse cross
sparse_cross = tf.raw_ops.SparseCross(
    indices=sparse_indices,
    values=sparse_values,
    dense_inputs=[dense_tensor],
    dense_shape=sparse_shape,
    device_ordinal=0
)

# Print the result
print(sparse_cross)
