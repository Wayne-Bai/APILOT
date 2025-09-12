import tensorflow as tf

# Create a sparse tensor from a list of non-zero indices and values
indices = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
values = [1.0, 2.0, 3.0, 4.0, 5.0]
sparse_tensor = tf.SparseTensor(indices, values)

# Reshape the sparse tensor to a new dense shape
dense_shape = [5, 10]
reshaped_sparse_tensor = tf.raw_ops.SparseReshape(sparse_tensor, dense_shape)
