import tensorflow as tf

# Define the log directory
log_dir = 'path/to/log_directory'

# Create a summary file writer
writer = tf.summary.create_file_writer(log_dir)
