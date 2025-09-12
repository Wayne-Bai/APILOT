import tensorflow as tf

def sparse_tensor_row_split(sparse_tensor):
    indices = sparse_tensor.indices
    dense_shape = sparse_tensor.dense_shape
    values = sparse_tensor.values

    # Splitting the tensor row-wise
    row_splits = tf.split(values, dense_shape[0], axis=0)
    row_splits = [tf.SparseTensor(indices=tf.boolean_mask(indices, tf.equal(indices[:, 0], i)),
                                 values=tf.boolean_mask(values, tf.equal(indices[:, 0], i)),
                                 dense_shape=[1, dense_shape[1]]) for i in range(dense_shape[0])]
    return row_splits
