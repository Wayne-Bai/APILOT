
import tensorflow as tf

# Define the variables to be updated
weight = tf.Variable(initial_value=0.1)
bias = tf.Variable(initial_value=-0.2)

# Define the sparse updates
indices = [[0], [1], [3]]
values = [1.5, 2.0, -3.0]
dense_shape = [4]

# Use tf.raw_ops.SparseTensorUpdate to update the variables
with tf.compat.v1.Session() as sess:
  sess.run(tf.global_variables_initializer())
  sparse_update_op = tf.raw_ops.SparseTensorUpdate(resource=weight, indices=indices, values=values, dense_shape=dense_shape)
  sess.run(sparse_update_op)
  updated_weights = sess.run(weight)
  print("Updated weights:", updated_weights)

  sess.run(tf.global_variables_initializer())
  sparse_update_op = tf.raw_ops.SparseTensorUpdate(resource=bias, indices=indices, values=values, dense_shape=dense_shape)
  sess.run(sparse_update_op)
  updated_bias = sess.run(bias)
  print("Updated bias:", updated_bias)
