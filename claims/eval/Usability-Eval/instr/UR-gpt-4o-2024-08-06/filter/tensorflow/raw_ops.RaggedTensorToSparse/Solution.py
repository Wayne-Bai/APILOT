import tensorflow as tf

# Sample ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [], [4, 5]])

# Create a SparseTensor from the RaggedTensor
sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_tensor())

print("Sparse Tensor Indices:\n", sparse_tensor.indices.numpy())
print("Sparse Tensor Values:\n", sparse_tensor.values.numpy())
print("Sparse Tensor Dense Shape:\n", sparse_tensor.dense_shape.numpy())
