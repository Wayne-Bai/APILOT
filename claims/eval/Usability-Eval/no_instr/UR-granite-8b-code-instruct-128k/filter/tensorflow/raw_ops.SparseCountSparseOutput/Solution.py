import tensorflow as tf

sparse_input = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
sparse_counts = tf.sparse.bincount(sparse_input, minlength=8, maxlength=10)

with tf.Session() as sess:
    result = sess.run(sparse_counts)

print(result)
