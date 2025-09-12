
import tensorflow as tf

# Create a sparse tensor
sparse_tensor = tf.SparseTensor(
    indices=[[0, 1], [1, 1], [2, 1]],
    values=[1, 0, 1],
    dense_shape=[3, 1])

# Split the sparse tensor into 2 tensors along the first dimension
num_splits = 2
split_sparse_tensors = tf.raw_ops.split_sparse_real_n_along_dim()

