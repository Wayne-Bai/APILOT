import tensorflow as tf

# Create a simple TensorFlow graph
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = tf.add(x, y)

# Start a new TensorFlow session
with tf.Session() as sess:
    # Feed data into the graph and fetch the output
    result1 = sess.run(z, feed_dict={x: 1.0, y: 2.0})
    print("Result 1: ", result1)

    # Continue the execution with more feeds and fetches
    result2 = sess.run(z, feed_dict={x: 3.0, y: 4.0})
    print("Result 2: ", result2)
