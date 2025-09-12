import tensorflow as tf

def create_file_writer(log_dir):
    """
    Creates a summary file writer for the given log directory.

    Args:
        log_dir (str): The directory where the summary files will be written.

    Returns:
        tensorflow.summary.SummaryWriter: A summary file writer.
    """
    return tf.summary.create_file_writer(log_dir=log_dir)

# Usage
writer = create_file_writer(log_dir="./logs")
