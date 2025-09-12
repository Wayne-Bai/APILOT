import tensorflow as tf

# Create a trace instance
trace = tf.profiler.Trace()

# Start the trace
trace.start()

# Run your code here
...

# End the trace
trace.stop()

# Print the trace information
print(trace)
