import tensorflow as tf

# Specify the log directory
log_dir = 'my_logs'  # Change this to your desired log directory

# Create the TensorBoard summary file writer
writer = tf.summary.create_file_writer(log_dir)

# Now you can write summaries using writer
