import tensorflow as tf

# Define the graph
a = tf.placeholder(tf.float32, shape=[], name='a')
b = tf.placeholder(tf.float32, shape=[], name='b')
c = tf.placeholder(tf.float32, shape=[], name='c')

# Define operations
sum_ab = tf.add(a, b, name='sum_ab')
result = tf.multiply(sum_ab, c, name='result')

# Create a session
with tf.Session() as sess:
    # Initialize variables
    sess.run(tf.global_variables_initializer())

    # Define feeds and fetches for partial run
    feeds = {a: 2.0, b: 3.0}
    fetches = [sum_ab]

    # Run the partial graph
    partial_result = sess.run(fetches, feed_dict=feeds)
    print("Partial result (sum_ab):", partial_result)

    # Now, use the partial result to complete the full computation
    feeds = {sum_ab: partial_result[0], c: 4.0}
    fetches = [result]

    # Run the full graph
    final_result = sess.run(fetches, feed_dict=feeds)
    print("Final result (result):", final_result)
