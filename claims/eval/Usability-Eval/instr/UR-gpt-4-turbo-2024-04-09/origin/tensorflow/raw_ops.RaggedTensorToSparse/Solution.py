import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Convert the RaggedTensor to a SparseTensor
    sparse_tensor = tf.sparse.from_dense(tf.RaggedTensor.to_tensor(ragged_tensor))
    return sparse_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [3], [], [4, 5, 6]])
sparse_tensor = ragged_to_sparse(ragged_tensor)
print("Sparse Tensor:")
print("Indices:", sparse_tensor.indices.numpy())
print("Values:", sparse_tensor.values.numpy())
print("Dense Shape:", sparse_tensor.dense_shape.numpy())
