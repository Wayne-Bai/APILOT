import tensorflow as tf

# Define the SparseTensor and dense Tensor
sparse_tensor = tf.sparse.from_dense([[1, 2], [3, 4], [5, 6]])
dense_tensor = tf.constant([2, 2], dtype=tf.float32)

# Perform the sparse tensor division using tf.raw_ops.SparseTensorDenseDiv
result = tf.raw_ops.SparseTensorDenseDiv(sp_indices=sparse_tensor.indices,
                                        sp_values=sparse_tensor.values,
                                        sp_shape=sparse_tensor.dense_shape,
                                        dense=dense_tensor)

# Print the result
print(result)
