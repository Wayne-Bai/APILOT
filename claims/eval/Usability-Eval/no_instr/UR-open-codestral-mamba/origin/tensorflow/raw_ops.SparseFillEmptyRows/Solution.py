import tensorflow as tf

# SparseTensor input with empty rows
indices = [[0, 0], [1, 0], [1, 1], [3, 0]]
values = [1, 2, 3, 4]
shape = [4, 2]
sparse_tensor = tf.sparse.SparseTensor(indices, values, shape)

# Default value to fill empty rows
default_value = 0

# Convert SparseTensor to RaggedTensor
ragged_tensor = tf.sparse.to_dense(sparse_tensor)

# Convert RaggedTensor to SparseTensor (replacing empty rows with default value)
default_filled_sparse_tensor = tf.sparse.from_dense(
    ragged_tensor, default_value=default_value)

print(default_filled_sparse_tensor)
