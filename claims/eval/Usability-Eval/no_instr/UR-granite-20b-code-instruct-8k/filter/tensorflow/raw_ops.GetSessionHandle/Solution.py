import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Store the input tensor in the state of the current session
tensor_handle = tf.identity(input_tensor).op.get_session_handle()
