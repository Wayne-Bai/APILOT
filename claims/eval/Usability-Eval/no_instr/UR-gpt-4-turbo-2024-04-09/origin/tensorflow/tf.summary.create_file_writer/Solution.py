import tensorflow as tf

# Specify the log directory
log_dir = "/path/to/your/log/directory"

# Create a summary file writer
writer = tf.summary.create_file_writer(log_dir)
