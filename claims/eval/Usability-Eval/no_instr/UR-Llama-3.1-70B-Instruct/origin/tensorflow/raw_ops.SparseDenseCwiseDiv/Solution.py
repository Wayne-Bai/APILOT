import tensorflow as tf

# Create a sparse tensor
sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 2], [2, 4]],
    values=[1., 2., 3.],
    dense_shape=[3, 5]
)

# Create a dense tensor
dense_tensor = tf.constant([[1., 2., 3., 4., 5.],
                            [6., 7., 8., 9., 10.],
                            [11., 12., 13., 14., 15.]])

# Perform component-wise division using tf.raw_ops.SparseTensorDenseMatMul
result_sparse_tensor = tf.raw_ops.SparseTensorDenseMatMul(
    a=sparse_tensor,
    b=tf.linalg.inv(dense_tensor),
    adjoint_b=False,
    adjoint_a=False,
)

# Convert the sparse tensor to dense
result_dense_tensor = tf.sparse.to_dense(result_sparse_tensor)

# Print the result
print(result_dense_tensor)
