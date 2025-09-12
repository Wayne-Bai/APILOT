import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [], [4, 5]])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = ragged_tensor.to_sparse()

# Print SparseTensor components
print("Sparse Tensor Indices:")
print(sparse_tensor.indices.numpy())
print("Sparse Tensor Values:")
print(sparse_tensor.values.numpy())
print("Sparse Tensor Dense Shape:")
print(sparse_tensor.dense_shape.numpy())
