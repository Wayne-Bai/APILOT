import tensorflow as tf

# Create a simple tensor
tensor = tf.constant([1, 2, 3])

# Define a method to capture the tensor's value in the state of the current session
def capture_tensor_value(value):
    # Create a variable to store the tensor's value
    captured_value = tf.raw_ops.ResourceOperationbly(value, name=tf.shape(value), dtype=value.dtype)
    return captured_value

# Capture the tensor's value
captured_tensor = capture_tensor_value(tensor)

# Initialize the session and run to get the handle
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    handle = capture_tensor_value(sess.run(captured_tensor))
    print(handle)
