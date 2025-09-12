
import tensorflow as tf

# Create a sparse tensor from a list of values and indices
sparse_values = [1, 2, 3]
sparse_indices = [[0, 0], [0, 1], [1, 1]]
sparse_dense_shape = [2, 2]
sparse_tensor = tf.SparseTensor(sparse_values, sparse_indices, dense_shape=sparse_dense_shape)

# Create a dense tensor from a list of values
dense_values = [1, 2, 3]
dense_tensor = tf.constant(dense_values, shape=[2, 2])

# Perform component-wise division of the sparse tensor by the dense tensor
result = tf.sparse_tensor_dense_matmul(sparse_tensor, dense_tensor)

print(result)
