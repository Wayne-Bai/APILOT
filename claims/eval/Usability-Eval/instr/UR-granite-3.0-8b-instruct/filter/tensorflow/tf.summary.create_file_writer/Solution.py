import tensorflow as tf

# Create a summary file writer for the given log directory
log_dir = "logs/"
summary_writer = tf.summary.create_file_writer(log_dir)
