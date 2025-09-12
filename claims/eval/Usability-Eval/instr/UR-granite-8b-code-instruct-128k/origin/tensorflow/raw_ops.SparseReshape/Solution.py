import tensorflow as tf

# Define the SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Reshape the SparseTensor to a new dense shape
reshaped_sparse_tensor = tf.sparse_reshape(sparse_tensor, [12])

# Convert the reshaped SparseTensor to a dense tensor
dense_tensor = tf.sparse_tensor_to_dense(reshaped_sparse_tensor)

# Print the resulting dense tensor
print(dense_tensor)
