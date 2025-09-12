import tensorflow as tf

# Define the graph
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = tf.add(x, y)

# Start a TensorFlow session
with tf.Session() as sess:
    # Initialize the variables
    sess.run(tf.global_variables_initializer())

    # Define the feeds and fetches
    feeds = {x: 1.0, y: 2.0}
    fetches = [z]

    # Run the session and get the result
    result = sess.run(fetches, feeds)
    print(result)  # Output: [3.0]
