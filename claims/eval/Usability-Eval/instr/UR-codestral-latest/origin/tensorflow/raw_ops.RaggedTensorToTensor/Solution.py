import tensorflow as tf

ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
dense_tensor = ragged_tensor.to_tensor(default_value=0)

print(dense_tensor)
