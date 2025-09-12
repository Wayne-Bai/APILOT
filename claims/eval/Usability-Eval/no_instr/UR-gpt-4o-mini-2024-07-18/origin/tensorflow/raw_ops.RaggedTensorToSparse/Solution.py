import tensorflow as tf

# Creating a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2], [], [3, 4, 5]])

# Converting the RaggedTensor to a SparseTensor
sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_sparse())

# Displaying the SparseTensor
print("SparseTensor values:", sparse_tensor.values.numpy())
print("SparseTensor indices:", sparse_tensor.indices.numpy())
print("SparseTensor dense_shape:", sparse_tensor.dense_shape.numpy())
