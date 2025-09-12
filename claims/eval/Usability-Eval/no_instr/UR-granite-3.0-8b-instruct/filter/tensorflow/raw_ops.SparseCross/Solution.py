import tensorflow as tf

# Assuming you have a list of sparse and dense tensors
sparse_tensors = [tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[2, 3])]
dense_tensors = [tf.constant([[1, 0, 0], [0, 1, 0]])]

# Concatenate sparse and dense tensors
concatenated_tensors = tf.concat(values=[sparse_tensors, dense_tensors], axis=0)

# Generate sparse cross from the concatenated tensors
sparse_cross = tf.raw_ops.SparseCross(sparse_tensors=concatenated_tensors, num_rows=2, num_cols=3)

print(sparse_cross)
