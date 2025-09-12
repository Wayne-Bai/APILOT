import tensorflow as tf

# Create a TensorFlow session
sess = tf.Session()

# Define a tensor to store in the session
tensor = tf.constant([1, 2, 3])

# Store the tensor in the session's state
sess.run(tf.assign(tensor, [4, 5, 6]))

# Create a handle to the tensor's value in the session
handle = tf.contrib.framework.make_tensor_proto(tensor, dtype=tf.float32)

# Print the handle
print(handle)
