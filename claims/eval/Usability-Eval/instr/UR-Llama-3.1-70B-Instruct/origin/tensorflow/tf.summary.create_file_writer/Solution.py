import tensorflow as tf

def create_summary_file_writer(log_dir):
    """
    Creates a summary file writer for the given log directory.

    Args:
        log_dir (str): Directory where the summary event files will be written.

    Returns:
        tf.summary.SummaryWriter: A summary writer for the given log directory.
    """
    # Check if the log directory exists, if not create it
    if not tf.io.gfile.exists(log_dir):
        tf.io.gfile.makedirs(log_dir)

    # Create a summary file writer for the given log directory
    summary_writer = tf.summary.create_file_writer(log_dir)

    return summary_writer


# Example usage:
log_dir = "./logs"
writer = create_summary_file_writer(log_dir)
with writer.as_default():
    tf.summary.scalar("loss", 0.1, step=1)
    tf.summary.scalar("accuracy", 0.9, step=1)

writer.close()
