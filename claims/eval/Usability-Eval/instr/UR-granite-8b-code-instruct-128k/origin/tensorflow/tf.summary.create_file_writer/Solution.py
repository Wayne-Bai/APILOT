import tensorflow as tf

# Set the log directory
log_dir = "/path/to/log/directory"

# Create a summary file writer
summary_writer = tf.summary.create_file_writer(log_dir)
