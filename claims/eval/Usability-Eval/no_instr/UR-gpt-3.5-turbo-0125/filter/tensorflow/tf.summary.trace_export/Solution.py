
import tensorflow as tf

# Define the path for the summary and profiler log files
summary_writer = tf.summary.create_file_writer("logs/summary_logs")
profiler_writer = tf.profiler.experimental.Profiler("logs/profiler_logs")

# Start the trace for profiling
with profiler_writer.as_default():
    tf.summary.trace_on(graph=True, profiler=True)
    # Your code for model training or evaluation goes here

    tf.summary.trace_export(name="trace", step=0, profiler_outdir="logs/profiler_logs")
