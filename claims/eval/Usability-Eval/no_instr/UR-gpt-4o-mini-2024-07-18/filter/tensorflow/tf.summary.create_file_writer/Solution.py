import tensorflow as tf

log_dir = "logs/"
summary_writer = tf.summary.create_file_writer(log_dir)

with summary_writer.as_default():
    tf.summary.text("example_text", "Hello, TensorFlow!", step=0)
