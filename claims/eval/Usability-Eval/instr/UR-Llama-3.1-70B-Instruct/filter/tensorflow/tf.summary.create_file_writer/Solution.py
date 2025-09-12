import tensorflow as tf

def create_summary_writer(log_dir):
    """
    Creates a summary file writer for the given log directory.

    Args:
        log_dir (str): The directory where the summary event files will be written.

    Returns:
        tf.summary.SummaryWriter: A summary writer that writes to the given log directory.
    """
    # Create a summary writer that writes to the given log directory
    summary_writer = tf.summary.create_file_writer(log_dir)

    return summary_writer

# Example usage:
if __name__ == "__main__":
    log_dir = "logs"
    summary_writer = create_summary_writer(log_dir)

    # Write a scalar summary to the event file
    with summary_writer.as_default():
        tf.summary.scalar("loss", 0.1, step=1)

    # Close the summary writer to flush the event file
    summary_writer.close()
