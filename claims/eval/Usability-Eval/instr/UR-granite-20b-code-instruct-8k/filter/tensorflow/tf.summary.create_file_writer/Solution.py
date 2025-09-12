import tensorflow as tf

def create_summary_file_writer(log_dir):
    summary_writer = tf.summary.create_file_writer(log_dir)
    return summary_writer
