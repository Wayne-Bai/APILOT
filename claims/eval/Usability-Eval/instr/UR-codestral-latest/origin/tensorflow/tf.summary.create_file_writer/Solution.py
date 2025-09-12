import tensorflow as tf
from tensorflow.summary import create_file_writer

# Define the log directory
log_dir = "path_to_your_log_directory"

# Create a file writer for the log directory
writer = create_file_writer(log_dir)
