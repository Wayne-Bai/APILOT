import tensorflow as tf

def sparse_bin_counting(input_indices, input_values, input_shape, weights=None, size_splits=None):
    sparse_tensor = tf.SparseTensor(indices=input_indices, values=input_values, dense_shape=input_shape)
    result = tf.raw_ops.SparseSegmentSum(data=sparse_tensor.values, segment_ids=sparse_tensor.indices[:, 0], num_segments=tf.reduce_max(sparse_tensor.indices[:, 0]) + 1)
    if weights is not None:
        result = tf.multiply(result, weights)
    if size_splits is not None:
        result = tf.split(result, size_splits)
    return result
