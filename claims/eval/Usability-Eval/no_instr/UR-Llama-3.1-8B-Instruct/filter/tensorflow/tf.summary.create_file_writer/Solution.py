# Import necessary libraries
import tensorflow as tf
import os

def create_summary_file_writer(log_directory):
    """
    Creates a summary file writer for the given log directory.

    Args:
    log_directory (str): The path to the log directory.

    Returns:
    A FileWriter object for the given log directory.
    """

    # Check if the log directory exists, if not create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create a summary writer
    # We use 'events' as the filename for the summary writer file
    summary_writer = tf.summary.create_file_writer(os.path.join(log_directory, 'events'))

    return summary_writer

# Example usage:
log_dir = '/path/to/log/directory'
writer = create_summary_file_writer(log_dir)
print(writer)
