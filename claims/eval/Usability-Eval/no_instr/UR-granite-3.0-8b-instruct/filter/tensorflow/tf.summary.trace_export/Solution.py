import tensorflow as tf

# Start a trace
tf.profiler.experimental.start('/tmp/tf_profiler')

# Your code here

# Stop the trace and export the results
tf.profiler.experimental.stop()
