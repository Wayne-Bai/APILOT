import os
import tensorflow as tf

def create_summary_file_writer(log_dir):
    """Creates a summary file writer for the given log directory."""
    return tf.summary.create_file_writer(log_dir)
