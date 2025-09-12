import tensorflow as tf

# define the log directory
log_dir = "path/to/your/logs"

# create a FileWriter to log the results of our model
summary_writer = tf.summary.create_file_writer(log_dir)
