import tensorflow as tf

# Assuming 'sp' is your SparseTensor
sp = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Split the SparseTensor into num_split tensors along one dimension
num_split = 2
sp_split = tf.raw_ops.Split(sp, num_split, axis=1)

print(sp_split)
