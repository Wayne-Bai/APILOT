
import tensorflow as tf

# Create a variable and a sparse tensor
var = tf.Variable(tf.zeros([10, 10]), dtype=tf.float32)
indices = tf.constant([[1, 2], [4, 6]])
values = tf.constant([-1., -2.])

# Assign the sparse updates to the variable
sparse_update_op = tf.raw_ops.ResourceSparseAssign(
    var=var, indices=indices, values=values)

# Run the assignment operation
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  sess.run(sparse_update_op)
