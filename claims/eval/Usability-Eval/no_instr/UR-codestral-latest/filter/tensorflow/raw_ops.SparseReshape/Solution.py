import tensorflow as tf

# Create a sparse tensor
indices = [[0, 0], [1, 2], [2, 4]]
values = [1, 2, 3]
dense_shape = [3, 6]
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Define the new shape
new_shape = [2, 3, 2]

# Reshape the sparse tensor
new_sparse_tensor = tf.sparse.reshape(sparse_tensor, new_shape)

# Check the new shape of the sparse tensor
print("New sparse tensor shape: ", new_sparse_tensor.shape)
