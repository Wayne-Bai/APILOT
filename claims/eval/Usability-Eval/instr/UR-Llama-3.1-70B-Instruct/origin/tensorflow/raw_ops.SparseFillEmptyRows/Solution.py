import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    """
    Fills empty rows in the input 2-D SparseTensor with a default value.

    Args:
    sparse_tensor: A 2-D SparseTensor.
    default_value: The value to fill the empty rows with.

    Returns:
    A SparseTensor with the empty rows filled.
    """
    # Get the dense shape of the SparseTensor
    dense_shape = sparse_tensor.dense_shape

    # Find the indices of non-empty rows
    row_indices, _ = tf.unique(tf.reshape(sparse_tensor.indices[:, 0], [-1]))

    # Create a tensor of indices for the empty rows
    empty_row_indices = tf.sets.difference(
        tf.constant([i for i in range(dense_shape[0])], dtype=row_indices.dtype),
        row_indices
    )

    # Create a new SparseTensor with the indices and values for the empty rows
    filled_sparse_tensor = tf.SparseTensor(
        indices=tf.expand_dims(empty_row_indices, axis=1),
        values=tf.constant(default_value, dtype=sparse_tensor.values.dtype, shape=[empty_row_indices.shape[0]]),
        dense_shape=dense_shape
    )

    # Combine the original SparseTensor with the new one
    result_sparse_tensor = tf.sparse.add(sparse_tensor, filled_sparse_tensor)

    return result_sparse_tensor


# Example usage
if __name__ == "__main__":
    # Create a SparseTensor
    sparse_tensor = tf.sparse.SparseTensor(
        indices=[[0, 0], [1, 2], [2, 4]],
        values=[1, 2, 3],
        dense_shape=[4, 5]
    )

    # Fill the empty rows with a default value
    filled_sparse_tensor = fill_empty_rows(sparse_tensor, 0)

    # Print the result
    print(filled_sparse_tensor)
