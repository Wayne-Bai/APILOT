import tensorflow as tf

# Create a tensor
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)

# Create a Variable to store the tensor's value
stored_tensor = tf.Variable(tf.zeros_like(input_tensor), trainable=False)

# Assign the value of the input_tensor to the Variable
assign_op = stored_tensor.assign(input_tensor)

# Function to run the operation and capture the value
def run_session_and_store():
    # Initialize the variables
    init = tf.compat.v1.global_variables_initializer()

    # Start a TensorFlow session
    with tf.compat.v1.Session() as sess:
        # Initialize variables
        sess.run(init)
        
        # Run the assignment operation
        sess.run(assign_op)
        
        # Capture the stored tensor's value
        result = sess.run(stored_tensor)
        
        return result

captured_value = run_session_and_store()
print("Captured Value:", captured_value)
