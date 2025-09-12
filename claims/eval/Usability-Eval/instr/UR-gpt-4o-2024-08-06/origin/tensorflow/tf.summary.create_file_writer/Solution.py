import tensorflow as tf

# Specify the log directory
logdir = "logs/my_runs/"

# Create a summary file writer
file_writer = tf.summary.create_file_writer(logdir)

# Example of using the writer to log a scalar value
with file_writer.as_default():
    for step in range(100):
        # Log a scalar (and this example logs step as the value)
        tf.summary.scalar("my_scalar_metric", step, step=step)
