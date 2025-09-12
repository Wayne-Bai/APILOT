import tensorflow as tf

# Create a sparse tensor with the necessary updates
sparse_indices = [[0, 0], [1, 2]]
sparse_values = [1, 2]
sparse_shape = [2, 3]
sparse_tensor = tf.SparseTensor(sparse_indices, sparse_values, sparse_shape)

# Create a dense tensor
dense_shape = [2, 3]
initial_dense_value = tf.zeros(dense_shape)

# Apply the sparse updates to the dense tensor
result = tf.raw_ops.SparseApplyRmsProp(
    var=initial_dense_value,
    indices=sparse_indices,
    lr=0.01,
    alpha=0.9,
    momentum=0.9,
    epsilon=1e-07,
    centered=False,
    values=sparse_values,
    delta=0.0,
)

print(result)
