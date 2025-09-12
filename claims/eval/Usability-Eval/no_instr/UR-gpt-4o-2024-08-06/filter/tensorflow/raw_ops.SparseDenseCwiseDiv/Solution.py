import tensorflow as tf

# Define a simple SparseTensor
sparse_values = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
sparse_indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
sparse_shape = tf.constant([3, 4], dtype=tf.int64)
sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_values, dense_shape=sparse_shape)

# Define a dense tensor
dense_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0], 
                            [1.0, 2.0, 3.0, 4.0], 
                            [1.0, 2.0, 3.0, 4.0]], dtype=tf.float32)

# Perform component-wise division
result_sparse_tensor = tf.sparse.SparseTensor(
    indices=sparse_tensor.indices,
    values=tf.divide(sparse_tensor.values, tf.gather_nd(dense_tensor, sparse_tensor.indices)),
    dense_shape=sparse_tensor.dense_shape
)

# Convert sparse tensor result to dense format for viewing
result_dense_tensor = tf.sparse.to_dense(result_sparse_tensor)

# For viewing the result
print("SparseTensor indices:\n", result_sparse_tensor.indices.numpy())
print("SparseTensor values:\n", result_sparse_tensor.values.numpy())
print("Dense representation:\n", result_dense_tensor.numpy())
