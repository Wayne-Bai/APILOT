import tensorflow as tf

# Define the sparse tensor.
indices = [[0, 0], [1, 2], [2, 3]]
values = [1, 2, 3]
dense_shape = [3, 4]
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Define the dense tensor.
dense_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=tf.float32)

# Component-wise divide the sparse tensor by the dense tensor.
sparse_div_dense = tf.divide(sparse_tensor.values, dense_tensor)

# Recreate the sparse tensor with the new values.
divided_sparse_tensor = tf.SparseTensor(indices, sparse_div_dense, dense_shape)
