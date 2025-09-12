
import tensorflow as tf

def create_summary_file_writer(log_dir):
    return tf.summary.create_file_writer(log_dir)

# Example usage:
log_dir = "/path/to/your/log/directory"
file_writer = create_summary_file_writer(log_dir)
