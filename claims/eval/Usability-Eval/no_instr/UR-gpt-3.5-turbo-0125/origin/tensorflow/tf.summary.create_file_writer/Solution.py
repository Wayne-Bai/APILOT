
import tensorflow as tf

log_dir = "logs/fit"  # Specify the log directory

summary_writer = tf.summary.create_file_writer(log_dir)  # Create a summary file writer

# Use the summary_writer with context manager to write summaries
with summary_writer.as_default():
    tf.summary.scalar("loss", 0.5, step=1)
