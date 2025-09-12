import tensorflow as tf

# Define the log directory
log_directory = "/path/to/your/log/directory"

# Create a summary file writer
summary_writer = tf.summary.create_file_writer(log_directory)

# Use the summary writer for writing summaries
with summary_writer.as_default():
    tf.summary.scalar("example_metric", 0.8, step=10)
    tf.summary.text("text_example", "This is an example text summary.")
