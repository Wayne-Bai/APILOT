import tensorflow as tf

# Create a session
sess = tf.Session()

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0])

# Get the lower-level TensorFlow operation to capture a tensor's value
capture_value_op = tf.raw_ops.CaptureValue(tensor)

# Run the operation to get a handle to the tensor's value
value_handle = sess.run(capture_value_op)

# Print the value handle
print(value_handle)

# Destroy the session
sess.close()
