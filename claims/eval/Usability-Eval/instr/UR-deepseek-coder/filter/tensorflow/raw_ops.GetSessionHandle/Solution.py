import tensorflow as tf

# Define a placeholder for the input tensor
input_tensor = tf.placeholder(tf.float32, shape=[None, None])

# Create a variable to store the tensor value
tensor_value_var = tf.Variable(tf.zeros_like(input_tensor), validate_shape=False)

# Operation to assign the input tensor to the variable
assign_op = tf.assign(tensor_value_var, input_tensor)

# Initialize the variable
init_op = tf.global_variables_initializer()

# Create a session
with tf.Session() as sess:
    # Initialize the variable
    sess.run(init_op)
    
    # Run the assign operation to store the input tensor in the variable
    input_value = [[1.0, 2.0], [3.0, 4.0]]
    sess.run(assign_op, feed_dict={input_tensor: input_value})
    
    # Retrieve the stored tensor value
    stored_value = sess.run(tensor_value_var)
    print("Stored Tensor Value:", stored_value)
