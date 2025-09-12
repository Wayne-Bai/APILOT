
import tensorflow as tf

input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
ones_tensor = tf.ones_like(input_tensor)

print(ones_tensor)
