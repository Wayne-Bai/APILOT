import tensorflow as tf

sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
new_shape = [2, 8]
reshaped_sparse_tensor = tf.sparse.reshape(sparse_tensor, new_shape)
