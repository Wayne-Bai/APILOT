import tensorflow as tf

# Create a sparse tensor with indices, values, and dense shape
indices = [[0, 0], [1, 2]]
values = [2.0, 3.0]
dense_shape = [3, 4]

sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Create a dense tensor
dense_tensor = tf.constant([[4.0, 5.0, 6.0, 7.0],
                            [8.0, 9.0, 10.0, 11.0],
                            [12.0, 13.0, 0.0, 14.0]])

# Perform component-wise division of sparse_tensor by dense_tensor
result = tf.raw_opsSparseTensorToDense(
    sparse=tf.raw_ops.SparseTensorToDense(sparse=sparse_tensor, default_value=0),
    dense=dense_tensor,
    name=None
)

print(result)
