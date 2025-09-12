import tensorflow as tf
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
dense_tensor = tf.ragged.to_tensor(ragged_tensor)
print(dense_tensor)
