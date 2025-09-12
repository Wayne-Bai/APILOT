import tensorflow as tf

sparse = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
tensor = tf.constant([[3, 4], [5, 6], [7, 8]])

result = tf.raw_ops.sparse_dense_cwise_div(sparse, tensor)

with tf.Session() as sess:
    print(sess.run(result))
