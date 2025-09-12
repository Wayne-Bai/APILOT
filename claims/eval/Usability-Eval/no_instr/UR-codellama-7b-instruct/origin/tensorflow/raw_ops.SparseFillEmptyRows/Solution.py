
import tensorflow as tf

sparse_tensor = ... # A 2-D SparseTensor
default_value = ... # The default value to use for filling empty rows
output_shape = ... # The shape of the output tensor

# Create a sparse tensor with the same non-empty indices, but filled with the default value
filled_sparse_tensor = tf.raw_ops.SparseFillEmptyRows(
    input=sparse_tensor,
    index_type=tf.int64, # The type of the row indices
    dims=output_shape, # The shape of the output tensor
    value=default_value, # The default value to use for filling empty rows
    name=None # Optional name for the operation
)
