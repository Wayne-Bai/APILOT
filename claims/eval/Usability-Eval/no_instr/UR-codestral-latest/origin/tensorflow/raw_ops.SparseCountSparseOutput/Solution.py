import tensorflow as tf

def sparse_bin_counting(sparse_input, size=None, weights=None):
    return tf.raw_ops.SparseSparseSegmentMean(indices=sparse_input.indices,
                                              values=sparse_input.values,
                                              segment_ids=sparse_input.dense_shape[0],
                                              sparse_output=True,
                                              size=size,
                                              weights=weights)

# Example usage:
sparse_tensor_input = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1.0, 2.0], dense_shape=[3, 4])
output = sparse_bin_counting(sparse_tensor_input)
