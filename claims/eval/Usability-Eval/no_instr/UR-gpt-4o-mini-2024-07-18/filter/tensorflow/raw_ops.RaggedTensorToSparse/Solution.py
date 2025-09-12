import tensorflow as tf

# Example usage of converting a RaggedTensor to a SparseTensor
# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [], [4, 5]])

# Convert RaggedTensor to SparseTensor
sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_dense())

# Print SparseTensor details
print("SparseTensor values:", sparse_tensor.values)
print("SparseTensor indices:", sparse_tensor.indices)
print("SparseTensor dense_shape:", sparse_tensor.dense_shape)
