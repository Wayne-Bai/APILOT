import tensorflow as tf

def ragged_to_sparse(rt):
    values = tf.reshape(rt.values, [-1])
    flat_indices = tf.reshape(tf.repeat(rt.row_splits, repeats=rt.row_lengths(), axis=0), [-1])
    dense_shape = tf.cast(tf.shape(rt, out_type=tf.int64), tf.int64)
    indices = tf.stack([flat_indices[:-1], rt.value_rowids()], axis=-1)
    sparse = tf.SparseTensor(indices, values, dense_shape)
    return sparse
