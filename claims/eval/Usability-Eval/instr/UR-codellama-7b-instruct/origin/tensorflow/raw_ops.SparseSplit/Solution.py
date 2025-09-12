import tensorflow as tf

# Create a sparse tensor
sp_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2], [3, 4]], values=[1, 2, 3], dense_shape=[5, 5])

# Split the sparse tensor into two parts along the first dimension
split_tensors = tf.raw_ops.SplitV(
    split_dim=0,
    size_splits=[sp_tensor.dense_shape[0] // 2, sp_tensor.dense_shape[0] - (sp_tensor.dense_shape[0] // 2)],
    value_list=[sp_tensor])
