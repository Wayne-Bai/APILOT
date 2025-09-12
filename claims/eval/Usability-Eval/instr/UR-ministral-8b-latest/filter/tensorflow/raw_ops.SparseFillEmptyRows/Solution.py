import tensorflow as tf

def fill_empty_rows_with_default(sparse_tensor, default_value):
    # Create a dense tensor from the sparse tensor
    dense_tensor = tf.raw_ops.Constant(sparse_tensor.indices, sparse_tensor.values, sparse_tensor.shape.dims)

    # Find the empty rows
    empty_rows = tf.where(sparse_tensor.indices[0] == 0)

    # Fill the empty rows with the default value
    filled_dense_tensor = dense_tensor + tf.fill(empty_rows, default_value)

    # Convert back to SparseTensor
    new_sparse_tensor = tf.raw_ops.SparseToDense(filled_dense_tensor)
    return new_sparse_tensor

# Example usage:
sparse_tensor = tf.raw_ops.SparseToDense(indices=tf.ragged.constant([[[0, 1], [1, 2], [2, 4]]]),
                                         values=tf.constant([1, 2, 3]),
                                         shape=(4, 5))

filled_tensor = fill_empty_rows_with_default(sparse_tensor, 0)
print(filled_tensor)
