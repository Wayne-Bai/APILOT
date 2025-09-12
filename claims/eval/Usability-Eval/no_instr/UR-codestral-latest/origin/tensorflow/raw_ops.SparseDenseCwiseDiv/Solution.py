import tensorflow as tf

# Creating a SparseTensor
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Creating a dense Tensor
dense_tensor = tf.constant([1, 2, 3, 4], shape=[2, 2])

# Component-wise divides a SparseTensor by a dense Tensor
result = tf.raw_ops.SparseTensorDenseMatMul(sparse_a=sparse_tensor, dense_b=tf.math.reciprocal(dense_tensor))
