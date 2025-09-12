import tensorflow as tf

# Create a new summary file writer
logdir = "logs/profile"
file_writer = tf.summary.create_file_writer(logdir)

# Start a trace
tf.profiler.experimental.start(logdir)

# Perform some operations
a = tf.constant([1.0, 2.0, 3.0], name='a')
b = tf.constant([4.0, 5.0, 6.0], name='b')
c = tf.add(a, b, name='c')

# Stop the trace
tf.profiler.experimental.stop()

# Export the trace as a summary
with file_writer.as_default():
    tf.summary.trace_export(name="my_trace", step=0, profiler_outdir=logdir)
