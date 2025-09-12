import tensorflow as tf

sparse_tensor = tf.sparse.constant([[1, 2], [3, 4], [5, 6]])
dense_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

result = tf.raw_ops.sparse_dense_cwise_div(sparse_tensor, dense_tensor)

print(result)
