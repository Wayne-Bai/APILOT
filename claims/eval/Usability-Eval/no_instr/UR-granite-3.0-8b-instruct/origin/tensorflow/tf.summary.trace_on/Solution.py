import tensorflow as tf

# Start a trace to record computation graphs and profiling information
tf.profiler.experimental.start('path/to/your/trace')

# Your TensorFlow code here

# Stop the trace
tf.profiler.experimental.stop()
