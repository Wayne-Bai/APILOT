
import tensorflow as tf

# Create a session and add a feed dictionary
with tf.Session() as sess:
    # Define the input data
    input_data = np.array([[1, 2], [3, 4]])

    # Create a graph with a single layer of neurons
    x = tf.placeholder(tf.float32, shape=[None, None])
    y = tf.layers.dense(x, units=1)

    # Define the loss function and optimizer
    loss = tf.reduce_mean(tf.square(y - x))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

    # Create a feed dictionary for the input data
    feed_dict = {x: input_data}

    # Initialize the variables
    sess.run(tf.global_variables_initializer())

    # Perform a partial run on the graph to calculate the loss and gradients
    fetches = [loss, optimizer._minimize]
    loss_val, _ = sess.partial_run(fetches=fetches, feed_dict=feed_dict)

# Print the loss value
print("Loss:", loss_val)
