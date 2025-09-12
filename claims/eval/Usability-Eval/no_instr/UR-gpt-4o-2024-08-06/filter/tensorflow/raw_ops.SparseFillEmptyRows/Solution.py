import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    # Convert SparseTensor components to dense tensors
    dense_shape = tf.convert_to_tensor(sparse_tensor.dense_shape)
    indices = tf.convert_to_tensor(sparse_tensor.indices)
    values = tf.convert_to_tensor(sparse_tensor.values, dtype=tf.float32)

    # Use the `tf.sparse.SparseTensor` to create a sparse tensor from indices and values
    st = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

    # Fill the empty rows in the SparseTensor
    filled_sparse_tensor, empty_row_indicator = tf.raw_ops.SparseFillEmptyRows(
        indices=indices,
        values=values,
        dense_shape=dense_shape,
        default_value=default_value
    )

    return filled_sparse_tensor, empty_row_indicator

# A sample sparse tensor
example_sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2], [2, 2]],
    values=[1, 2, 3],
    dense_shape=[4, 3]
)

# Fill empty rows with default value, e.g., 0
filled_sparse_tensor, empty_row_indicator = fill_empty_rows(example_sparse_tensor, default_value=0)

tf.print(filled_sparse_tensor)
tf.print(empty_row_indicator)  # Indicator showing which rows were empty and filled
