import tensorflow as tf

# Create a variable to store the input tensor
input_tensor = tf.Variable(initial_value=input_data, trainable=False)

# Initialize the variable
init = tf.variables_initializer([input_tensor])

# Start a session and run the initialization operation
with tf.Session() as sess:
    sess.run(init)
