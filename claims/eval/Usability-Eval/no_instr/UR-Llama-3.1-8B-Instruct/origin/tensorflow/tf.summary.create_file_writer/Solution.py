# Import the necessary libraries
import tensorflow as tf

# Define the log directory where the summaries will be saved
log_dir = './logs'

# Create a summary writer for the given log directory
summary_writer = tf.summary.create_file_writer(log_dir)

# You can start writing logs to this summary writer here
# For example, you can write a scalar value like this:
# tf.summary.scalar('loss', loss_value, step=100)
# Or you can write a scalar value per promotional with the `experimental_git 커'  쟁İR cuenta'
