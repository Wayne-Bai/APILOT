import tensorflow as tf

# Create a SparseTensor
indices = tf.constant([[1, 2], [3, 5]])
values = tf.constant([4.0, 5.0])
shape = tf.constant([6, 6])

sparse_tensor = tf.SparseTensor(indices, values, shape)

# Print the original SparseTensor
print("Original SparseTensor:")
print(sparse_tensor)

# Get the original dense shape
dense_shape = tf.sparse.dense_shape(sparse_tensor)

# Specify the new dense shape (1, 3, 2) for reshaping
new_dense_shape = [1, 3, 2]

# Use tf.sparse.reshape to reshape the SparseTensor
reshaped_sparse_tensor = tf.sparse.reshape(sparse_tensor, new_dense_shape)

# Print the reshaped SparseTensor
print("\nReshaped SparseTensor:")
print(reshaped_sparse_tensor)

# Convert the SparseTensor to a dense tensor
reshaped_dense_tensor = tf.sparse.to_dense(reshaped_sparse_tensor)

# Print the reshaped dense tensor
print("\nReshaped Dense Tensor:")
print(reshaped_dense_tensor)
