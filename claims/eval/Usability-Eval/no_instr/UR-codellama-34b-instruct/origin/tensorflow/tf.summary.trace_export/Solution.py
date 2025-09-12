import tensorflow as tf

# Create a summary writer
writer = tf.summary.create_file_writer('path/to/output/directory')

# Write the summary and profile data
with writer.as_default():
    tf.summary.trace_export(step=10)
