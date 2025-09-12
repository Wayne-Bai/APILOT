import tensorflow as tf

# Create a sparse tensor
indices = [[0, 0], [1, 2]]
values = [1.0, 2.0]
dense_shape = [3, 4]
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Create a dense tensor
dense_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                            [5.0, 6.0, 7.0, 8.0],
                            [9.0, 10.0, 11.0, 12.0]])

# Perform the division operation
result_sparse_tensor = tf.math.divide_no_nan(sparse_tensor, dense_tensor)

# Print the result
print(result_sparse_tensor)
