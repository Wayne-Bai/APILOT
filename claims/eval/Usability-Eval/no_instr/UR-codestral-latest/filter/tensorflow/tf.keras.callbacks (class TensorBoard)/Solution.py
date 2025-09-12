import tensorflow as tf

# Create a log writer object
writer = tf.summary.create_file_writer('logs')

# Create some tensors
a = tf.constant(10, name='a')
b = tf.constant(5, name='b')

# Use TensorFlow operations
c = tf.add(a, b, name='add')

# Create TensorFlow summary operations
tf.summary.scalar('c_scalar', c)

# Write the summaries to the log directory
with writer.as_default():
    tf.summary.scalar('c_scalar', c)
    tf.summary.histogram('a_histogram', a)

# Run a TensorFlow session to execute the operations and write the summaries
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    merged_summary_op = tf.summary.merge_all()
    summary = sess.run(merged_summary_op)
    writer.add_summary(summary)

# Close the writer
writer.close()
