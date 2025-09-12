import tensorflow as tf
import os

# Set directory where profile logs are stored
logdir = './logs/'

# Create a file writer for the log directory
file_writer = tf.summary.create_file_writer(logdir)

# Start a trace for profiling
tf.summary.trace_on(graph=True, profiler=True)

# Example function to trace
@tf.function
def my_traced_function(x, y):
    return x * y + y

# Call the traced function
result = my_traced_function(tf.constant(3), tf.constant(5))

# Stop the trace and export the trace log
with file_writer.as_default():
    tf.summary.trace_export(
        name="my_trace",
        step=0,
        profiler_outdir=logdir
    )

print("Profiling data has been saved to:", os.path.abspath(logdir))
