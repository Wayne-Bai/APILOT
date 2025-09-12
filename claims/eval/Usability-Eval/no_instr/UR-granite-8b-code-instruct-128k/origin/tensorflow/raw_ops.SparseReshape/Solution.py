import tensorflow as tf

# Create a SparseTensor
values = [1, 2, 3, 4, 5, 6]
indices = [[0, 0], [1, 2], [2, 1]]
dense_shape = [3, 3]
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Reshape the SparseTensor
new_dense_shape = [3, 2]
reshaped_sparse_tensor = tf.sparse_reshape(sparse_tensor, new_dense_shape)

# Convert the reshaped SparseTensor to a dense tensor
dense_tensor = tf.sparse_tensor_to_dense(reshaped_sparse_tensor)

# Print the resulting dense tensor
print(dense_tensor)
