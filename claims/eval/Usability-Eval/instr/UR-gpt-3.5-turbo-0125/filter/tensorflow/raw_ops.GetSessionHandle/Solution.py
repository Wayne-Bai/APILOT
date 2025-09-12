
import tensorflow as tf

# Create a variable to store the input tensor
input_tensor = tf.placeholder(tf.float32)

# Store the input tensor in the state of the current session
handle = tf.raw_ops.VarHandleOp(dtype=tf.float32)

# Initialize the handle with the value of the input tensor
init_handle = tf.raw_ops.AssignVariableOp(resource=handle, value=input_tensor)

with tf.Session() as sess:
    sess.run(init_handle, feed_dict={input_tensor: 5.0})

# 'handle' now contains the value of the input tensor in the session
