import tensorflow as tf

# Placeholder for input
input_placeholder = tf.placeholder(tf.float32, shape=(None, 784))

# Define variables and operations for the graph
weight = tf.Variable(tf.random.normal([784, 10]))
bias = tf.Variable(tf.zeros([10]))

# Operation to compute the output
output_operation = tf.matmul(input_placeholder, weight) + bias

# Create session for partial run
with tf.Session() as sess:
    # Only initialize the variables used in this part of the graph
    sess.run(tf.variables_initializer([weight, bias]))

    # Define the feed dictionary with input data
    feed_dict = {input_placeholder: input_data}

    # Perform the partial graph computation
    partial_output = sess.run([output_operation], feed_dict=feed_dict)
