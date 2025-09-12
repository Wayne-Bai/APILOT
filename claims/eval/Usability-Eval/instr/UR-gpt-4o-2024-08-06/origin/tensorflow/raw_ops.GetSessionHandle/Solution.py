import tensorflow as tf

# Create a simple tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])

# Use the tf.Variable to store the tensor in the session state
stored_input_tensor = tf.Variable(input_tensor)

# Initialize the variables
init_op = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    # Run the initializer op
    sess.run(init_op)
    
    # Get the handle to the stored tensor's value
    handle_value = sess.run(stored_input_tensor)
    
    print("Handle value of the stored input tensor:", handle_value)
