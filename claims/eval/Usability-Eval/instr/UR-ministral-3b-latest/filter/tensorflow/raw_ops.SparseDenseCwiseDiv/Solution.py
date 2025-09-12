import tensorflow as tf

# Define the SparseTensor
sparse_indexes = [[[0]], [[2]], [[1]]]
sparse_values = tf.constant([[1.0, 2.0]])

sparse_tensor = tf.sparse.SparseTensor(sparse_indexes, sparse_values, shape=[3])

# Define the dense Tensor
dense_tensor = tf.constant([[1.0, 3.0, 5.0]])

# Perform the component-wise division
result = tf.sparse.psum(tf.sparse.sparse_div(sparse_tensor, dense_tensor), axes=[1])

print(result)
