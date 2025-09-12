
import tensorflow as tf

def fill_empty_rows(input_indices, input_values, input_shape, default_value):
    filled_sparse_tensor = tf.raw_ops.SparseFillEmptyRows(indices=input_indices, values=input_values, dense_shape=input_shape, default_value=default_value)
    return filled_sparse_tensor
