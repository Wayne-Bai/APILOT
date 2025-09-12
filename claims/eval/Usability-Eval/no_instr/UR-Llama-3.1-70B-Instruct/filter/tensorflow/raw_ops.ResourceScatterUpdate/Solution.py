import tensorflow as tf

# Create a tensorflow variable with initial values
x = tf.Variable([[1, 2], [3, 4]], dtype=tf.int32)

# Create indices and values for sparse update
indices = tf.constant([[0, 0], [1, 1]])
values = tf.constant([5, 6])

# Use tf.raw_ops.AssignVariable to assign sparse updates
assign_op = tf.raw_ops.AssignVariableOp(resource=x, indices=indices, value=values)

# Run the assign operation in a tensorflow session
with tf.Session() as sess:
    sess.run(assign_op)
    # Print the updated variable value
    print(sess.run(x))
