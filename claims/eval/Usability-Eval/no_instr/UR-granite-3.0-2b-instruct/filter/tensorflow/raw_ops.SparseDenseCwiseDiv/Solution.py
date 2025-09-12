import tensorflow as tf

# Define a dense tensor
dense_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Define a sparse tensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1]], values=[[5.0], [6.0]], dense_shape=[2, 2])

# Use tf.raw_ops.SparseDenseTensorDivision to perform component-wise division
result = tf.raw_ops.SparseDenseTensorDivision(sparse_tensor, dense_tensor)

# Print the result
print(result)
