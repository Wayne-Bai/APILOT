import tensorflow as tf

# Start a trace to record computation graph and profiling information
tf.profiler.experimental.start('logdir')

# Code to profile, can be any heavy computation or a model training loop

# Stop the profiler and save the summarized information
tf.profiler.experimental.stop()
