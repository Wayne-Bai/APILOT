import tensorflow as tf

def create_summary_writer(log_dir):
    # Creates a summary writer for the specified log directory
    writer = tf.summary.create_file_writer(log_dir)
    return writer

# Example usage:
log_directory = "./logs"
writer = create_summary_writer(log_directory)

# Using the writer to write summaries
with writer.as_default():
    for step in range(100):
        # Record a simple scalar value summary
        tf.summary.scalar("my_scalar", step * 1.0, step=step)

# You may flush and close the writer
writer.flush()
writer.close()
