import tensorflow as tf

log_dir = 'path/to/log/directory'
writer = tf.summary.create_file_writer(log_dir)
