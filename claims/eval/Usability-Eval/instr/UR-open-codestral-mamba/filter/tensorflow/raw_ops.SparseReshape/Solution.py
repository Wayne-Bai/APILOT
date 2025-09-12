import tensorflow as tf

# Sparse tensor initializing
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Reshaping the sparse tensor
reshaped_tensor = tf.sparse.reshape(sparse_tensor, [6, 2])

print(reshaped_tensor)
