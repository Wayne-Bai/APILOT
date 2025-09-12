import tensorflow as tf

# Start a trace to record computation graphs and profiling information
tf.profiler.experimental.start('log_dir')

# Add code here that you want to profile

# Stop the profiler and save the profiling information to 'log_dir'
tf.profiler.experimental.stop()
