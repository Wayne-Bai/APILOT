import tensorflow as tf

# Create a variable
variable = tf.Variable(initial_value=tf.constant([0, 0, 0]))

# Create a placeholder for input tensor
input_tensor = tf.placeholder(tf.int32, shape=[3])

# Operation to update the variable with the value of the input tensor
assign_op = tf.raw_ops.AssignVariableOp(ref=variable, value=input_tensor)

# Initialize global variables
init_op = tf.global_variables_initializer()

# Start session
with tf.Session() as sess:
    sess.run(init_op)

    # Value to be stored in the variable
    input_values = [1, 2, 3]

    # Run the operation to update the variable
    handle = sess.run(assign_op, feed_dict={input_tensor: input_values})

    # Print the updated variable value
    print(sess.run(variable))
