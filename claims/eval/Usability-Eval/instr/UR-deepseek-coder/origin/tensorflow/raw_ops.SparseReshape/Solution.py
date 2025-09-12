import tensorflow as tf

def sparse_reshape(sparse_tensor, new_shape):
    # Get the indices, values, and dense shape of the input SparseTensor
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    dense_shape = sparse_tensor.dense_shape

    # Compute the new indices and dense shape
    new_indices, new_dense_shape = tf.sparse.to_dense(
        tf.sparse.reshape(sparse_tensor, new_shape)
    )

    # Create a new SparseTensor with the new indices, values, and dense shape
    reshaped_sparse_tensor = tf.SparseTensor(
        indices=new_indices,
        values=values,
        dense_shape=new_dense_shape
    )

    return reshaped_sparse_tensor

# Example usage:
# Assuming you have a SparseTensor `sparse_tensor` and a new shape `new_shape`
# reshaped_sparse_tensor = sparse_reshape(sparse_tensor, new_shape)
