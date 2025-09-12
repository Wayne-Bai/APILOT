import tensorflow as tf

# Define the log directory for storing the summary files
log_dir = "./logs"

# Create a summary file writer using the log directory
summary_writer = tf.summary.create_file_writer(log_dir)

# Example usage of the summary writer to log a scalar value
with summary_writer.as_default():
    tf.summary.scalar('example_metric', 0.5, step=1)

# Make sure to flush the writer at the end of the logging
summary_writer.flush()
