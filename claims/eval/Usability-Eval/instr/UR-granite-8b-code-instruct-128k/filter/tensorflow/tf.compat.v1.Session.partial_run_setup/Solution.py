import tensorflow as tf

# Create a graph with feeds and fetches for partial run.
g = tf.Graph()
with g.as_default():
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)
    z = tf.multiply(x, y)

    # Define a saver to save and restore variables.
    saver = tf.train.Saver()

# Create a session and initialize variables.
with tf.Session(graph=g) as sess:
    # Initialize variables.
    sess.run(tf.global_variables_initializer())
    # Save the variables to disk.
    save_path = saver.save(sess, "/tmp/model.ckpt")