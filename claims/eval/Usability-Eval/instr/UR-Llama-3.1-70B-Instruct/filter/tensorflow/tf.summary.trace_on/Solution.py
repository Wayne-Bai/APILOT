import tensorflow as tf

# Create a TensorFlow session
sess = tf.Session()

# Define a simple computation graph
a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a, b)

# Start tracing
tf.compat.v1.run(tf.compat.v1.assign(tf.compat.v1.get_collection('traces')[0], True))

# Run the computation graph, which will be traced
result = sess.run(c)

# Stop tracing
tf.compat.v1.run(tf.compat.v1.assign(tf.compat.v1.get_collection('traces')[0], False))

# Print the result
print("Result: ", result)

# Get the timeline object
run_metadata = tf.compat.v1.RunMetadata()
run_options = tf.compat.v1.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)

# Create a profile object
profiler = tf.compat.v1.profiler.Profiler(sess.graph)

# Print profiling information
profiler.add_step(1, run_metadata)
profiler.profile_name_scope()
