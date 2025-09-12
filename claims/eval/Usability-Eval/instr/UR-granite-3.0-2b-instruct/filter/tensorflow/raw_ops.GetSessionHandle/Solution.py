import tensorflow as tf

# Create a session
sess = tf.Session()

# Create a tensor
tensor = tf.constant(5.0)

# Store the input tensor in the state of the current session
tensor_handle = sess.run(tf.raw_ops.CaptureTensorValue(tensor))

# Print the tensor value
print(tensor_handle.eval())
