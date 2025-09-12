import tensorflow as tf

def create_summary_file_writer(log_dir):
    writer = tf.summary.create_file_writer(log_dir)
    return writer
