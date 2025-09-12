import tensorflow as tf

# Define a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.sparse.SparseTensor(
    indices=ragged_tensor.indices,
    values=ragged_tensor.values,
    dense_shape=ragged_tensor.bounding_shape()
)

# For demonstration, convert the sparse tensor into its dense form
dense_tensor = tf.sparse.to_dense(sparse_tensor)

print("Sparse Tensor:")
print(sparse_tensor)

print("\nDense Tensor:")
print(dense_tensor)
