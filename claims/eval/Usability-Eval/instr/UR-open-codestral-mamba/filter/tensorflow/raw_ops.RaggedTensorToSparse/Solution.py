import tensorflow as tf

def convert_ragged_to_sparse(ragged_tensor):
    # Convert RaggedTensor to SparseTensor
    sparse_tensor = tf.sparse.SparseTensor(
        indices=ragged_tensor.indices,
        values=ragged_tensor.values,
        dense_shape=ragged_tensor.bounding_shape()
    )
    return tf.sparse.reorder(sparse_tensor)

# Example usage
ragged_tensor = tf.ragged.constant([[1, 2], [3, 4, 5], [6]])
print(tf.print(convert_ragged_to_sparse(ragged_tensor)))
