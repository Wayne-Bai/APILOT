import tensorflow as tf

# Define a tensor
input_tensor = tf.constant([1.0, 2.0, 3.0])

# Use Variable to store the input_tensor in the current session's state
state_variable = tf.Variable(input_tensor, name='state_variable')

# Initialize the variable
init_op = tf.compat.v1.global_variables_initializer()

# Create a session to run the initialization op
with tf.compat.v1.Session() as sess:
    # Initialize the variables
    sess.run(init_op)
    
    # Capture the stored value (handle)
    handle = state_variable.handle
    captured_value = sess.run(tf.raw_ops.ReadVariableOp(resource=handle, dtype=tf.float32))

    # Print the captured value
    print("Captured Value:", captured_value)
