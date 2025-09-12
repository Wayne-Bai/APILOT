import tensorflow as tf

# Create a SummaryWriter object for the given log directory
summary_writer = tf.summary.create_file_writer(log_dir)
