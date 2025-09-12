
import tensorflow as tf

# Create nodes in the graph, initialize placeholders and operations
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.add(a, b)

# Create a session to run the graph
with tf.Session() as sess:
    # Run the session with feeds and fetches for partial run
    output = sess.run(c, feed_dict={a: 5.0, b: 7.0})
    print(output)
