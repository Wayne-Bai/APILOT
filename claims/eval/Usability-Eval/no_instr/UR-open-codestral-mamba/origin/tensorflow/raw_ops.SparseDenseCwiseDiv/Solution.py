import tensorflow as tf

# Create a SparseTensor
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Create a dense Tensor
dense_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Divide the SparseTensor by the dense Tensor
result = tf.raw_ops.SparseTensorDenseDiv(sp_a=sparse_tensor, dense_b=tf.cast(dense_tensor, tf.float))

# Print the result
print(result)
