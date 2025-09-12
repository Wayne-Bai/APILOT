import tensorflow as tf

# Create a simple TensorFlow graph
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = tf.add(x, y)

# Define a saver to save and restore variables
saver = tf.train.Saver()

# Start a TensorFlow session
with tf.Session() as sess:

    # Initialize variables
    sess.run(tf.global_variables_initializer())

    # Define feeds and fetches
    feeds = {x: 10, y: 20}
    fetches = z

    # Perform partial run
    result = sess.partial_run( feeds=feeds, fetches=fetches)

    # Print the result
    print(result)
