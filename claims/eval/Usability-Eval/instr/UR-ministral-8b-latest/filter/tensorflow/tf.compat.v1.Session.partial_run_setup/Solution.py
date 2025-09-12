import tensorflow as tf

# Set up a graph
graph = tf.Graph()

# Define a session
with graph.as_default():
    # Define a constant tensor
    x = tf.constant(3.0, name='input')

    # Create an output tensor
    y = tf.add(x, x, name='add')

    # Create a feed dict for the inputs
    feed_dict = {x: 3.0}

    # Create a session
    with tf.Session(graph=graph) as sess:
        # Run the fetch operation
        output = sess.run(y, feed_dict=feed_dict)

    print(output)
