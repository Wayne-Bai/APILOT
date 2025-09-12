import tensorflow as tf

# Start the computational graph
a = tf.placeholder(tf.float32, shape=None, name='a')
b = tf.placeholder(tf.float32, shape=None, name='b')
c = tf.add(a, b, name='addition')

# Define feeds and fetches
feed_dict = {a: 2, b: 3}
fetch_list = [a, b, c]

# Define a partial run
with tf.Session() as sess:
    # Run the partial computation
    fetches = sess.run(fetch_list, feed_dict=feed_dict)

    # Print the results
    print(fetches)
