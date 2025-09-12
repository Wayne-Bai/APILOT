
import tensorflow as tf

# Start trace
tf.summary.trace_on(graph=True, profiler=True)

# Your code here

# Export the active trace as a summary and/or profile file
with tf.summary.create_file_writer('logs/trace').as_default():
    tf.summary.trace_export(
        name="trace",
        step=0,
        profiler_outdir='logs/trace'
    )
