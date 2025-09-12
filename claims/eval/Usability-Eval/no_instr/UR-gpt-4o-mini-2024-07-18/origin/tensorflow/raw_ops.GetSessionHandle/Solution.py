import tensorflow as tf

# Define a function to store a tensor in the current session state
def store_tensor_in_session(tensor):
    # Create a TensorFlow session
    with tf.Session() as sess:
        # Capture the value of the tensor
        tensor_value = sess.run(tensor)
        # Return the tensor value
        return tensor_value

# Example usage
if __name__ == "__main__":
    # Create a sample tensor
    input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int32)
    
    # Store the tensor in the session and get its value
    stored_value = store_tensor_in_session(input_tensor)
    print("Stored Tensor Value:", stored_value)
