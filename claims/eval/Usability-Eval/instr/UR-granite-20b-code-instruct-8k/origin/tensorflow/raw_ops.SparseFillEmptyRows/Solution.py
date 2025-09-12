import tensorflow as tf

# Define the input SparseTensor
sparse_tensor = tf.sparse.from_dense([[1, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [0, 0, 3, 0, 0],
                                       [4, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]])

# Define the default value to fill empty rows
default_value = 0

# Use tf.sparse.fill_empty_rows to fill empty rows in the SparseTensor
filled_sparse_tensor, empty_row_indicator = tf.sparse.fill_empty_rows(sparse_tensor, default_value)

# Print the filled SparseTensor
print(filled_sparse_tensor.numpy())
