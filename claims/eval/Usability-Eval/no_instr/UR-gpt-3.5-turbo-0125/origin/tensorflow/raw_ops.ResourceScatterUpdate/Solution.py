
import tensorflow as tf

# Define the variable to be updated
var = tf.Variable(tf.constant([[1.0, 2.0], [3.0, 4.0]]))

# Define the indices and updates for the sparse assignment
indices = tf.constant([[0, 0], [1, 1]])
updates = tf.constant([5.0, 6.0])

# Perform the sparse assignment using tf.raw_ops
update_op = tf.raw_ops.ResourceSparseApplyGradientDescent(var, indices=indices, values=updates, use_locking=False)

# Run the update operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(update_op)
    result = sess.run(var)
    print(result)
