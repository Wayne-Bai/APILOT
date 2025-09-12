import tensorflow as tf

# Specify the directory where the log files will be written
log_dir = "logs/"

# Create a summary file writer for the specified log directory
file_writer = tf.summary.create_file_writer(log_dir)

# Example: Use the file_writer to write a summary
with file_writer.as_default():
    tf.summary.scalar('example_metric', 0.5, step=1)

# Use this writer to log various metrics as needed in your training loop
