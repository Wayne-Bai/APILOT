import tensorflow as tf

def create_summary_writer(log_dir):
    summary_writer = tf.summary.create_file_writer(log_dir)
    return summary_writer

# Example usage:
log_dir = "./logs"
writer = create_summary_writer(log_dir)
