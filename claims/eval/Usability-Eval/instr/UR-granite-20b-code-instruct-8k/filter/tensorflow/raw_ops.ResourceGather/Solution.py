import tensorflow as tf
indices = tf.constant([[0, 0], [1, 2]])
updates = tf.constant([3.14, 2.78])
resource = tf.Variable([1.0, 2.0, 3.0, 4.0])
with tf.control_dependencies([resource.scatter_nd_update(indices, updates)]):
  result = resource.read_value()
print(result.numpy())
