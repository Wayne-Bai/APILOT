
import tensorflow as tf

# Define the input SparseTensor
sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1, 2],
    dense_shape=[3, 4]
)

# Define the default value to fill empty rows
default_value = -1

# Use tf.sparse_fill_empty_rows to fill empty rows with the default value
output, empty_row_indicator = tf.raw_ops.SparseFillEmptyRows(
    sparse_tensor=sparse_tensor,
    default_value=default_value
)

# Print the output SparseTensor and the empty row indicator
print("Output SparseTensor:", output.numpy())
print("Empty row indicator:", empty_row_indicator.numpy())
