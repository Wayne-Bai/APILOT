import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Get the values, row_splits, and row_lengths from the RaggedTensor
    values = ragged_tensor.values
    row_splits = ragged_tensor.row_splits
    row_lengths = ragged_tensor.row_lengths()

    # Create indices for the SparseTensor
    indices = tf.RaggedTensor.from_row_splits(
        values=tf.range(tf.size(values)),
        row_splits=row_splits
    ).to_tensor()

    # Create the SparseTensor
    sparse_tensor = tf.SparseTensor(
        indices=indices,
        values=values,
        dense_shape=tf.stack([tf.shape(row_splits)[0] - 1, tf.reduce_max(row_lengths)])
    )

    return sparse_tensor

# Example usage:
# ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
# sparse_tensor = ragged_to_sparse(ragged_tensor)
# print(sparse_tensor)
