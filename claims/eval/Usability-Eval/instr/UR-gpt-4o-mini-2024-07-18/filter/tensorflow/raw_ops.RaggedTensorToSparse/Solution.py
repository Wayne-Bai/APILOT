import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Convert the RaggedTensor to a SparseTensor
    sparse_tensor = tf.sparse.to_sparse_tensor(ragged_tensor)
    return sparse_tensor

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [], [3]])
sparse_tensor = ragged_to_sparse(ragged_tensor)

# To print the SparseTensor
print("SparseTensor indices:", sparse_tensor.indices.numpy())
print("SparseTensor values:", sparse_tensor.values.numpy())
print("SparseTensor dense_shape:", sparse_tensor.dense_shape.numpy())
