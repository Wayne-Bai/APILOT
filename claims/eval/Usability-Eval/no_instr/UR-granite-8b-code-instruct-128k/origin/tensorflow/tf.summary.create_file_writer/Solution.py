import tensorflow as tf

log_dir = "/path/to/log/directory"
summary_writer = tf.summary.create_file_writer(log_dir)
