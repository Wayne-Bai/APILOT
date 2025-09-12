import tensorflow as tf

# Create a resource variable
var = tf.Variable(initial_value=tf.zeros([10, 10]), dtype=tf.float32)

# Define sparse indices and updates
sparse_indices = tf.constant([[4, 3], [3, 6]])
sparse_updates = tf.constant([7.0, 1.0])

# Use the ResourceScatterDiv method to divide sparse updates by the values in the variable
updated_var = tf.raw_ops.ResourceScatterDiv(resource=var.handle, indices=sparse_indices, updates=sparse_updates)

# Apply the updates to the variable
with tf.control_dependencies([updated_var]):
    update_op = var.assign(var)

# Run the graph in a session
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    sess.run(update_op)
    print(sess.run(var))
