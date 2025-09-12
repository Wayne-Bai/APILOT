import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Convert RaggedTensor to SparseTensor
    sparse_tensor = tf.sparse.from_dense(ragged_tensor.to_dense())
    return sparse_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [], [3, 4, 5]])
sparse_tensor = ragged_to_sparse(ragged_tensor)

print("Sparse Tensor:")
print(sparse_tensor)
