import tensorflow as tf

# Create a 2-D SparseTensor
indices = tf.constant([[0, 0], [1, 2]], dtype=tf.int64)
values = tf.constant([10, 20], dtype=tf.int32)
shape = tf.constant([3, 4], dtype=tf.int64)
sparse_tensor = tf.sparse.SparseTensor(indices, values, shape)

# Fill empty rows with a default value
default_value = tf.constant(-1, dtype=tf.int32)
output, empty_row_indicator, _ = tf.raw_ops.SparseFillEmptyRows(
    sparse_tensor=sparse_tensor,
    default_value=default_value,
    name="sparse_fill_empty_rows"
)

# Print the output SparseTensor
print(output.eval())

# Print the empty row indicator
print(empty_row_indicator.eval())
