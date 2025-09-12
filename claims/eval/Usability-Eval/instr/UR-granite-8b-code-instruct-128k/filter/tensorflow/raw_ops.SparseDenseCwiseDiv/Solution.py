import tensorflow as tf

sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
dense_tensor = tf.constant([[3, 0, 0, 0], [0, 4, 0, 0], [0, 0, 5, 0]])
result = tf.sparse.sparse_dense_div(sparse_tensor, dense_tensor)

with tf.Session() as sess:
    print(sess.run(result))
