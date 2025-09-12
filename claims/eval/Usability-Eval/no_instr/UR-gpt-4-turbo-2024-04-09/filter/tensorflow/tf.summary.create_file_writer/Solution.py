import tensorflow as tf

log_dir = "./logs"
writer = tf.summary.create_file_writer(logdir=log_dir)
