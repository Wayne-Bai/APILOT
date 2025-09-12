
import tensorflow as tf

# Define the graph
x = tf.placeholder(tf.float32, shape=(None,))
y = tf.placeholder(tf.float32, shape=(None,))
z = x + y

# Create a session and run it with new feeds and fetches
with tf.Session() as sess:
  feed_dict = {x: [1., 2., 3.], y: [4., 5., 6.]}
  output, new_feed_dict = sess.run(z, feed_dict)
  print(output)  # Output: [5., 7., 9.]

  # Add more feeds and fetches to the session
  x = tf.placeholder(tf.float32, shape=(None,))
  y = tf.placeholder(tf.float32, shape=(None,))
  z = x * y

  feed_dict = {x: [10., 20., 30.], y: [40., 50., 60.]}
  output, new_feed_dict = sess.run(z, feed_dict)
  print(output)  # Output: [400., 800., 1200.]
