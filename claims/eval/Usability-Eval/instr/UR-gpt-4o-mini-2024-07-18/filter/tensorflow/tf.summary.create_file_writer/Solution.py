import tensorflow as tf

log_dir = "path/to/log_dir"
summary_writer = tf.summary.create_file_writer(log_dir)

# Example of using the writer
with summary_writer.as_default():
    tf.summary.scalar("example_metric", 0.5, step=1)
summary_writer.flush()  # Ensure that all pending events have been written to disk
