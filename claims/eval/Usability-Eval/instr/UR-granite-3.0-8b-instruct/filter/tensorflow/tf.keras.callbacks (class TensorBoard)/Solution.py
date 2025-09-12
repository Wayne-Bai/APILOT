import tensorflow as tf

# Create a TensorFlow summary writer
summary_writer = tf.summary.create_file_writer("path/to/log/dir")

# Example of writing a scalar summary
with summary_writer.as_default():
    tf.summary.scalar("loss", 0.1, step=1)

# Example of writing an image summary
with summary_writer.as_default():
    tf.summary.image("images", [tf.random.normal([1, 28, 28, 3])], step=1)

# Example of writing a text summary
with summary_writer.as_default():
    tf.summary.text("text", "This is a text summary", step=1)
