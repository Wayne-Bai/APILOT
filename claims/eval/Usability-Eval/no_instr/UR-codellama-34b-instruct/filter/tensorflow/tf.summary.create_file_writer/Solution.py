
import tensorflow as tf

# Define the path to the log directory
logdir = "path/to/your/log/directory"

# Create a summary file writer for the given log directory
file_writer = tf.summary.FileWriter(logdir, graph=tf.get_default_graph())
