import tensorflow as tf

# Defines the log directory.
log_dir = "/path/to/logs/directory"

# Creates a summary file writer.
summary_writer = tf.summary.create_file_writer(log_dir)

# Usage:
# with summary_writer.as_default():
#   tf.summary.scalar('metric_to_track', metric_tensor, step=epoch)
