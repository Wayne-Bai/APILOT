import tensorflow as tf

# Define a placeholder for the input tensor
input_tensor = tf.placeholder(tf.float32, shape=[None, None])

# Create a variable to store the input tensor
stored_tensor = tf.Variable(tf.zeros_like(input_tensor), validate_shape=False)

# Operation to assign the input tensor to the variable
assign_op = tf.assign(stored_tensor, input_tensor)

# Create a session
with tf.Session() as sess:
    # Initialize the variable
    sess.run(tf.global_variables_initializer())
    
    # Example input data
    input_data = [[1.0, 2.0], [3.0, 4.0]]
    
    # Run the assign operation to store the input tensor
    sess.run(assign_op, feed_dict={input_tensor: input_data})
    
    # Retrieve the stored tensor
    retrieved_tensor = sess.run(stored_tensor)
    
    print("Stored Tensor:", retrieved_tensor)
