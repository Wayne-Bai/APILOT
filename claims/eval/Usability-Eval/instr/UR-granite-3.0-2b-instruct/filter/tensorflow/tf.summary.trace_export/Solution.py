import tensorflow as tf

# Assuming 'trace' is the active trace
tf.summary.write('runs/my_run/trace')
tf.profiler.experimental.start('my_profile')

# Your code here

tf.profiler.experimental.stop('my_profile')
tf.summary.write('runs/my_run/trace')
