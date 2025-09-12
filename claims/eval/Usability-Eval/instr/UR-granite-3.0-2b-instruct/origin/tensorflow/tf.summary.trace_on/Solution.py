import tensorflow as tf

# Create a compute graph
a = tf.constant(5.0)
b = tf.constant(3.0)
c = tf.add(a, b)

# Start a trace
tf.compat.v1.trace.start_as_default_trace_scope()

# Perform some operations
d = tf.multiply(c, 2.0)
e = tf.square(d)

# Stop the trace
tf.compat.v1.trace.stop()

# Print the trace data
print(tf.compat.v1.trace.trace_data)
