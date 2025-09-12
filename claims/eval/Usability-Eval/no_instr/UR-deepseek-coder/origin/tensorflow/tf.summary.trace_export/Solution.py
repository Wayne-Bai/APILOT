import tensorflow as tf

# Start tracing
tf.summary.trace_on(graph=True, profiler=True)

# Your TensorFlow code here
# Example:
# a = tf.constant(2)
# b = tf.constant(3)
# c = tf.add(a, b)

# Stop tracing and export the trace as a Summary
with tf.summary.create_file_writer('logs').as_default():
    tf.summary.trace_export(
        name="my_trace",
        step=0,
        profiler_outdir='logs'
    )
