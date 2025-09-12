import tensorflow as tf

# Define the variable
variable = tf.Variable([[0.0, 1.0], [1.0, 2.0]], dtype=tf.float32)

# Define the updates
indices = [[0, 0], [1, 1]]
values = [[1.0], [2.0]]

# Update the variable
with tf.compat.v1.Session() as sess:
    sess.run(variable.initializer)
    for i in range(len(indices)):
        update = tf.raw_ops.AssignVariable(
                  variable_handle=variable.handle,
                  value=values[i]
        )
        sess.run(update)
    print(sess.run(variable.eval()))
