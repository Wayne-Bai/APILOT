import tensorflow as tf

# Create a TensorFlow graph
with tf.name_scope("my_graph"):
    # Define some operations
    a = tf.constant([1.0, 2.0])
    b = tf.constant([3.0, 4.0])
    c = tf.add(a, b)

    # Add a summary for each operation
    tf.summary.scalar('a', a)
    tf.summary.scalar('b', b)
    tf.summary.scalar('c', c)

    # Merge all summaries into a single Operation
    summary_op = tf.summary.merge_all()

    # Create a session and run the summary operation
    with tf.Session() as sess:
        summary_writer = tf.summary.FileWriter('logs/', sess.graph)
        summary = sess.run(summary_op)
        summary_writer.add_summary(summary)
