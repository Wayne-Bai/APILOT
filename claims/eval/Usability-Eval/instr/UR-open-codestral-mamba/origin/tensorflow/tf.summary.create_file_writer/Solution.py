import tensorflow as tf

# Define the log directory
logdir = "logs"

# Create a summary writer
writer = tf.summary.create_file_writer(logdir)

# Use the writer to write some data
with writer.as_default():
    tf.summary.scalar('accuracy', 0.65, step=100)
