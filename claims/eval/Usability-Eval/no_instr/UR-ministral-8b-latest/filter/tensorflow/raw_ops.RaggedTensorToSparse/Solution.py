import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    """Converts a RaggedTensor to a SparseTensor with the same values."""
    return tf.raw_ops.RaggedToSparse(ragged=ragged_tensor)

# Example usage
ragged = tf.ragged.constant([[1, 2], [3, 4, 5]])
sparse = ragged_to_sparse(ragged)
print(sparse)
