import tensorflow as tf

# Define a SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Define the new dense shape
new_dense_shape = [3, 4, 1]

# Use SparseReshape operation to reshape the SparseTensor
dense_tensor = tf.sparse.to_dense(sparse_tensor)
reshaped_tensor = tf.reshape(dense_tensor, new_dense_shape)

# Print the reshaped tensor
print(reshaped_tensor)
