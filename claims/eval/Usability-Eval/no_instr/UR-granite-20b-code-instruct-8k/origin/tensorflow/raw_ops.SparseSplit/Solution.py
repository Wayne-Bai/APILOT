import tensorflow as tf

sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
num_split = 2

output = tf.raw_ops.Split(sparse_handle=sparse_tensor, num_split=num_split, axis=1)

print(output)
