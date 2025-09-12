import tensorflow as tf

# Start tracing
tf.profiler.experimental.start

# Your code here

# Stop tracing and export the active trace
tf.profiler.experimental.stop
