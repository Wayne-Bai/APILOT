import tensorflow as tf

# Define indices, values, and dense_shape for a 2-D SparseTensor
indices = tf.constant([[0, 0], [1, 2], [3, 1]], dtype=tf.int64)
values = tf.constant([1, 2, 3], dtype=tf.int32)
dense_shape = tf.constant([4, 4], dtype=tf.int64)

# Create the SparseTensor
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define the default value to fill empty rows
default_value = tf.constant(0, dtype=tf.int32)

# Use tf.sparse.fill_empty_rows to fill empty rows with the default value
filled_sparse_tensor, empty_row_indicator = tf.sparse.fill_empty_rows(sparse_tensor, default_value)

# Evaluate the result (in eager mode this will work straightforward)
print("Filled SparseTensor indices:")
print(filled_sparse_tensor.indices.numpy())
print("Filled SparseTensor values:")
print(filled_sparse_tensor.values.numpy())
print("Empty row indicator:")
print(empty_row_indicator.numpy())
