import tensorflow as tf
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
dense_tensor = tf.sparse.to_dense(ragged_tensor)
