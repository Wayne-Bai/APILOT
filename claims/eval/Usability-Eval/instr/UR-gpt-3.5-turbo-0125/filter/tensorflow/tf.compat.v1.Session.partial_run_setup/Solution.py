
import tensorflow as tf

# Define graph operations
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.add(a, b)
d = tf.multiply(c, b)

# Create session and run the graph with feeds and fetches for partial run
with tf.Session() as sess:
    # Run the graph with partial run
    result = sess.run(d, feed_dict={a: 2.0, b: 3.0})
    print(result)
