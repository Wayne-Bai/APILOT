import tensorflow as tf

# Start a trace to record computation graphs and profiling information
tf.summary.trace_on(graph=True, profiler=True)

# Your TensorFlow code here
# Example:
# a = tf.constant(2)
# b = tf.constant(3)
# c = tf.add(a, b)

# Stop the trace and save the information
with tf.summary.create_file_writer('logs').as_default():
    tf.summary.trace_export(name="trace", step=0, profiler_outdir='logs')
