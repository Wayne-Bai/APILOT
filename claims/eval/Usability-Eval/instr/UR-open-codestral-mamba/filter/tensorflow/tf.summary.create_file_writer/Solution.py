import tensorflow as tf

# Create a summary writer
log_dir = "/path/to/log/directory"  # replace with your desired path
summary_writer = tf.summary.create_file_writer(log_dir)
