import tensorflow as tf

# Create a session and add some initial values to the graph
with tf.Session() as sess:
    # Add some initial values to the graph
    x = tf.constant(1)
    y = tf.constant(2)
    z = tf.add(x, y)

    # Run the graph and get the output
    result = sess.run([z])
    print(result)  # Output: [3]

# Add some more values to the graph and run it again
with tf.Session() as sess:
    x = tf.constant(5)
    y = tf.constant(10)
    z = tf.add(x, y)

    # Run the graph and get the output
    result = sess.run([z])
    print(result)  # Output: [15]
