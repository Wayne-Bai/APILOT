import tensorflow as tf

# Define the log directory
log_dir = "logs/"

# Create a summary file writer
summary_writer = tf.summary.create_file_writer(log_dir)

# Example of using summary writer
with summary_writer.as_default():
    for step in range(100):
        # Log a scalar value
        tf.summary.scalar('my_metric', step * 2, step=step)

# Make sure to flush and close the writer
summary_writer.flush()
summary_writer.close()
