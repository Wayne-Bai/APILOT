import tensorflow as tf
from tensorflow.python.framework import sparse_tensor

# Define sparse tensor
sparse_tensor_values = tf.constant([[1, 0, 2], [3, 0, 0], [0, 4, 5]], dtype=tf.int64)
sparse_tensor_indices = tf.constant([[0, 0], [0, 2], [1, 0], [1, 2], [2, 1]], dtype=tf.int64)
sparse_tensor_shape = tf.constant([3, 3])

sparse_tensor = sparse_tensor.SparseTensor(sparse_tensor_indices, sparse_tensor_values, sparse_tensor_shape)

# Reshape sparse tensor to a new dense shape
dense_shape = tf.constant([2, 3, 3])
new_sparse_tensor = tf.sparse.reshape(sparse_tensor, dense_shape)

print(type(new_sparse_tensor))
print(new_sparse_tensor.dense_shape)
print(new_sparse_tensor.indices)
print(new_sparse_tensor.values)
