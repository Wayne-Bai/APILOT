import tensorflow as tf

# Function to convert RaggedTensor to SparseTensor
def ragged_to_sparse(ragged_tensor):
    ragged_values = tf.raw_ops.RaggedTensorToFlatValues(ragged_tensor.values)
    ragged_row_indices = tf.raw_ops.RaggedTensorToFlatValues(ragged_tensor.row_indices)
    ragged_column_indices = tf.raw_ops.RaggedTensorToFlatValues(ragged_tensor.col_indices)

    return tf.sparse.SparseTensor(
        indices=[ragged_col_indices, ragged_row_indices],
        values=ragged_values,
        dense_shape=ragged_tensor.shape
    )

# Example usage
ragged = tf.ragged.constant([[1, 0], [1]])
sparse = ragged_to_sparse(ragged)
for val in sparse:
    print(val)
