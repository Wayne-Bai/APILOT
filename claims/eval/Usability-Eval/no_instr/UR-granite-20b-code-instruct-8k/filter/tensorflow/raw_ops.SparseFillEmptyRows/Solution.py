import tensorflow as tf

def fill_empty_rows_sparse_tensor(sparse_tensor, default_value):
    return tf.raw_ops.sparse_tensor_to_dense(sparse_tensor, default_value=default_value, validate_indices=False)
