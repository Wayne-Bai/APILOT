import tensorflow as tf

# Create a variable
var = tf.Variable(tf.random.normal([3, 4, 5]))

# Create indices
indices = tf.constant([[0, 0, 0], [1, 2, 3]])

# Gather slices from the variable
gathered_slices = tf.gather_nd(var, indices)

# Initialize the variable
init_op = tf.global_variables_initializer()

# Start a session
with tf.Session() as sess:
    sess.run(init_op)
    result = sess.run(gathered_slices)
    print(result)
