import tensorflow as tf

# Start a trace to record computation graphs and profiling information
tf.summary.trace_on(graph=True, profiler=True)

# Your TensorFlow operations and computations go here

# Stop the trace and export the recorded information
with tf.summary.create_file_writer('logs').as_default():
    tf.summary.trace_export(name="trace", step=0)
