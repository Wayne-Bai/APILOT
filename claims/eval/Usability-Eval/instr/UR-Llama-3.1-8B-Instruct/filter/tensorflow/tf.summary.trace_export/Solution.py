import tensorflow as tf

# Create a TensorFlow session
with tf.Session() as sess:
    # Define a graph to profile
    x = tf.placeholder(tf.float32)
    y = tf.square(x)

    # Add the graph to the default graph
    tf.summary.FileWriter('profile', sess.graph)

    # Initialize the session
    sess.run(tf.global_variables_initializer())

    # Add merging of 'tf.summary' events and 'tfamon' events
    merged_summary = tf.summary.merge_all()

    # Create a summary writer
    summary_writer = tf.summary.FileWriter('profile', flush_secs=10)

    # Export the active trace as a Summary and/or profile file
    for i in range(10):
        feed_dict = {x: [i]}
        summary_str = sess.run(merged_summary, feed_dict=feed_dict)
        summary_writer.add_summary(summary_str, i)

    # Close the summary writer
    summary_writer.close()

# Flush the summary writer to write the summary file
tf.summary.FileWriter('profile', flush_secs=1).close()
