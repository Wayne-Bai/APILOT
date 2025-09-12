
import tensorflow as tf

# Your code for defining the model, training, etc.

# Create a summary writer
log_dir = "logs/"
summary_writer = tf.summary.create_file_writer(log_dir)

# Define a function to log with TensorBoard
def log_to_tensorboard(epoch, loss, accuracy):
    with summary_writer.as_default():
        tf.summary.scalar('loss', loss, step=epoch)
        tf.summary.scalar('accuracy', accuracy, step=epoch)

# Your code for training loop, where you call log_to_tensorboard() to log metrics
