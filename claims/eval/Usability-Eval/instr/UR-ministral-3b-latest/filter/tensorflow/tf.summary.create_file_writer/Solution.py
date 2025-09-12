import tensorflow as tf

# Assuming log_dir is the directory where you want to write summaries
log_dir = '/path/to/log/dir'

# Create a summary file writer
summary_writer = tf.summary.create_file_writer(log_dir)

# Optionally, you can also create a TensorFlow graph summary, which automatically
# attaches the variable summaries to the graph (used for events and summaries written to the AbstractGraphomme):
#graph_summary = tf.summary.create_file_writer(log_dir, graph=model.summary_graph())

