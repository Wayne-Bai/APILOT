import tensorflow as tf

# Assuming we have a sparse tensor `sp_idx` and a tensor `bin_size`
sp_idx = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2], [2, 2]], values=[1, 2, 3], dense_shape=[3, 3])
bin_size = 1

# Convert the sparse tensor to a dense tensor
dense_sp_idx = tf.sparse.to_dense(sp_idx)

# Perform sparse-output bin counting using tf.raw_ops.RefreshableSparseBincount
binned_tensor = tf.raw_ops.RefreshableSparseBincount(input_ix=dense_sp_idx.indices, input_y=dense_sp_idx.values, bins_size=bin_size)

# Print the binning result
print(binned_tensor)
