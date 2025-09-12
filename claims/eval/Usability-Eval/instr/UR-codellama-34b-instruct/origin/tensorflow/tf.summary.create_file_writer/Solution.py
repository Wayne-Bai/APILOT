
import tensorflow as tf

# Create a summary file writer
summary_writer = tf.summary.create_file_writer("path/to/log/directory")

# Write summaries to the file
with summary_writer.as_default():
    summary = tf.Summary()
    summary.value.add(tag="loss", simple_value=10.0)
    summary_writer.write(summary)
