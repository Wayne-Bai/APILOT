import tensorflow as tf

def convert_ragged_to_sparse(ragged_tensor):
    # Convert the RaggedTensor to a SparseTensor
    sparse_tensor = tf.sparse.from_dense(tf.ragged.to_tensor(ragged_tensor))
    return sparse_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [3], [], [4, 5, 6]])
sparse_tensor = convert_ragged_to_sparse(ragged_tensor)
print("Sparse Tensor Indices:", sparse_tensor.indices.numpy())
print("Sparse Tensor Values:", sparse_tensor.values.numpy())
print("Sparse Tensor Dense Shape:", sparse_tensor.dense_shape.numpy())
