import tensorflow as tf

# Create a DTensor from a tf.DistributedVariable
layout = tf.DTensorSpec(tf.TensorShape([None, None]), tf.float32, 'layout')
d_var = tf.experimental.DTensor(tf.Variable(initial_value, shape=target_shape, name='d_var'), layout)
