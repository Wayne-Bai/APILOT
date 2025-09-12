import tensorflow as tf

# Define the shape and data type of the sparse tensor
sparse_shape = (3, 4)
sparse_values = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
sparse_indices = [[0, 0], [1, 1]]
sparse_tensor = tf.SparseTensor(sparse_values, sparse_indices, sparse_shape)

# Define the shape and data type of the dense tensor
dense_shape = (3, 4)
dense_values = [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
dense_tensor = tf.constant(dense_values, dtype=tf.float32)

# Perform component-wise division between the sparse and dense tensors
div_result = tf.raw_ops.SparseDivide(sparse_tensor, dense_tensor, name='div')
