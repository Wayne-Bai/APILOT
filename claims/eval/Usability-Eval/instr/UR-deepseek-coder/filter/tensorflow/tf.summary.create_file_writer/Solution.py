import tensorflow as tf

# Define the log directory
log_dir = "logs/"

# Create a summary file writer
summary_writer = tf.summary.create_file_writer(log_dir)

# Optionally, you can use the summary writer to write summaries
with summary_writer.as_default():
    tf.summary.scalar('example_metric', 42, step=1)
