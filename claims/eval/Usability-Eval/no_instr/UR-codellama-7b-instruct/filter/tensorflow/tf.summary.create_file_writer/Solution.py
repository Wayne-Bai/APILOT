
import tensorflow as tf

# Create a SummaryWriter to write logs and checkpoints
summary_writer = tf.summary.FileWriter('logs', tf.get_default_session())

# Write some values to the summary writer
summary_writer.add_summary(tf.Summary(value=[tf.Summary.Value(tag='my_tag', simple_value=10)], step=0))

# Flush the summary writer to write the summaries to disk
summary_writer.flush()
