# Import necessary libraries
import tensorflow as tf

# Create a TensorFlow session
sess = tf.Session()

# Start tracing
tf.summary.trace_on(graph=True, profiler=True)

# Perform some operations for tracing (for demonstration purposes)
a = tf.constant(1.0)
b = tf.constant(2.0)
c = tf.add(a, b)

# Run the operations
sess.run(c)

# Stop tracing and export the trace
trace = tf.summary.trace_off()

# Create a file writer to export the trace as a Summary
writer = tf.summary.FileWriter('./trace')
writer.add_summary(trace)
writer.close()

# Create a Profiler to export the profile as a profile file
profiler = tf.profiler.Profiler(sess.graph)

# Optionally, you can also use tf.profiler.profile to export the profile
# tf.profiler.profile(sess.graph, options=tf.profiler.ProfilerOptions(
#     host_tracer_level=2,
#     device_tracer_level=1,
# ))

profiler.add_trace_to_time_line(None, './timeline.json')

print("Trace and profile saved to./trace and./timeline.json")
