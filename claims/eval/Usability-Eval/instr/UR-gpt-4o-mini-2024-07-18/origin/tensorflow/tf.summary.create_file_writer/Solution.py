import tensorflow as tf

# Define the log directory
log_dir = "path/to/log_dir"

# Create a summary writer
summary_writer = tf.summary.create_file_writer(log_dir)

# Example usage: Writing a simple scalar value
with summary_writer.as_default():
    tf.summary.scalar('example_scalar', 42, step=1)
    summary_writer.flush()
