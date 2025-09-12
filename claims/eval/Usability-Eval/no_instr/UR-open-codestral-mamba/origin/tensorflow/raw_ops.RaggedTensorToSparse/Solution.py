import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    split_indices = tf.magged.range(ragged_tensor.row_splits[:-1], ragged_tensor.row_splits[1:], delta=1, dtype=tf.int32)
    sparse_tensor = tf.sparse.SparseTensor(
        indices=split_indices,
        values=ragged_tensor.values,
        dense_shape=ragged_tensor.dense_shape,
    )
    return tf.sparse.reorder(sparse_tensor)

# Testing the function
# Define a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])
print("RaggedTensor:")
print(ragged_tensor)

sparse_tensor = ragged_to_sparse(ragged_tensor)
print("\nSparseTensor:")
print(sparse_tensor)
