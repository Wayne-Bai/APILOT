import tensorflow as tf

# Create a variable and an initializer
var = tf.Variable(tf.zeros([10]))
init = tf.global_variables_initializer()

# Create indices and updates
indices = tf.constant([0, 3, 9])
updates = tf.constant([1.0, 2.0, 3.0])

# Create an operation that updates the variable using the sparse updates
update_operation = tf.scatter_update(var, indices, updates)

# Start the session and initialize the variable
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(var))  # Prints the initial value of the variable
    sess.run(update_operation)
    print(sess.run(var))  # Prints the updated value of the variable
