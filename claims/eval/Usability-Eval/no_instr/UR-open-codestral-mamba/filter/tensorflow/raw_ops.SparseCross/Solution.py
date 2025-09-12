import tensorflow as tf

# Assuming we have a list of sparse and dense tensors
sparse_tensors = [tf.SparseTensor(indices=[[0, 1], [1, 0]],
                                  values=[1, 2],
                                  dense_shape=[2, 2]),
                  tf.SparseTensor(indices=[[0, 1], [1, 0]],
                                  values=[3, 4],
                                  dense_shape=[2, 2])]
dense_tensors = [tf.constant([[1, 2], [3, 4]]),
                 tf.constant([[5, 6], [7, 8]])]

# Generate sparse cross from list of sparse and dense tensors
sparse_cross = tf.raw_ops.SparseCross(sparse_inputs=sparse_tensors,
                                      dense_inputs=dense_tensors,
                                      name=None)
print(sparse_cross)
