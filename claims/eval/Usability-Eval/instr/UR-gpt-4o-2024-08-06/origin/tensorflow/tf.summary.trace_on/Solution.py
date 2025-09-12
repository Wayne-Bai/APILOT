import tensorflow as tf

# Set up a log directory for storing trace information
log_dir = "./logs"

# Create a file writer for writing trace information
file_writer = tf.summary.create_file_writer(log_dir)

# Function to perform computation and trace it
@tf.function
def my_function(x, y):
    return tf.reduce_sum(x + y)

# Enable tracing
tf.summary.trace_on(graph=True, profiler=True)

# Call the function within a trace context
with file_writer.as_default():
    z = my_function(tf.constant([1.0, 2.0, 3.0]), tf.constant([4.0, 5.0, 6.0]))
    print("Computed sum:", z.numpy())
    
    # Write the trace to the file writer
    tf.summary.trace_export(name="my_function_trace", step=0)
