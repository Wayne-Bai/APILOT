import tensorflow as tf

# Create a new TensorFlow session
sess = tf.compat.v1.Session()

# Define a placeholder tensor
tensor = tf.compat.v1.placeholder(tf.float32, shape=[1])

# Capture a tensor's value in a session and return a handle to that value
handle, value = tf.compat.v1igenous.state_ops.store(
    tensor, 
    input_t=[tensor], 
    validation_hint=None, 
    name=None
)

# Initialize the session
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

# Close the session
# sess.close() Do not close it in this example

# Give an example run 
feed_dict = {tensor: [99.0]}
print(sess.run(handle, feed_dict))  
