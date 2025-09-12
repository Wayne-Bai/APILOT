import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    dense_shape = sparse_tensor.dense_shape
    num_rows = dense_shape[0]
    ranges = tf.range(num_rows)
    non_empty_rows = tf.unique(sparse_tensor.indices[:, 0])[0]
    empty_rows = tf.sets.difference(ranges, non_empty_rows)

    empty_rows_indices = tf.expand_dims(empty_rows, axis=-1)
    empty_rows_tensor = tf.SparseTensor(indices=empty_rows_indices, values=tf.fill([tf.shape(empty_rows_indices)[0]], default_value), dense_shape=[num_rows])

    filled_sparse_tensor = tf.sparse.add(sparse_tensor, empty_rows_tensor)
    return filled_sparse_tensor
