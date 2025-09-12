import tensorflow as tf

# Set up a graph
g = tf.Graph()

with g.as_default():
    # Create a variable and an operation
    var = tf.Variable(tf.zeros([3]), name='var')
    op = tf.assign(var, var + 1, name='op')

    # Define feeds and fetches
    feed_dict = {var: tf.constant([1, 2, 3])}
    fetches = [var, op]

    # Create a session
    sess = tf.Session(graph=g)

    try:
        # Run the operation
        result = sess.run(fetches, feed_dict=feed_dict)
        print("Partial Run Result:")
        print(result)
    finally:
        # Close the session
        sess.close()
