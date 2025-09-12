import tensorflow as tf

# Define a function to store a tensor and return its handle
def store_tensor_in_session(tensor):
    # Define a variable to hold the tensor value
    tensor_variable = tf.Variable(tensor, trainable=False, dtype=tensor.dtype)

    # Initialize the variable
    init = tf.compat.v1.global_variables_initializer()

    # Create a session
    with tf.compat.v1.Session() as sess:
        sess.run(init)
        # Get the handle to the tensor variable
        handle = tensor_variable.handle
        return handle

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4]])
tensor_handle = store_tensor_in_session(input_tensor)
print("Tensor handle:", tensor_handle)
