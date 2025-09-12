import tensorflow as tf

# Start tracing
tf.summary.trace_on(graph=True, profiler=True)

# Your TensorFlow operations here
# ...

# Stop tracing and export the trace as a Summary
with tf.summary.create_file_writer('logs').as_default():
    tf.summary.trace_export(
        name="my_trace",
        step=0,
        profiler_outdir='logs'
    )
