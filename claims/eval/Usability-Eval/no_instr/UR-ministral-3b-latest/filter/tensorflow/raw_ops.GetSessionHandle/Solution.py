import tensorflow as tf

# Create a session object
with tf.Session() as sess:
    # Create a constant tensor
    constant_tensor = tf.constant(1, name='constant_tensor')

    # Store the tensor in the session's state
    session_handle = sess.run(constant_tensor)

    # Capture the tensor's value
    captured_tensor = tf.raw_ops.Status.Store(session_handle)
