import tensorflow as tf

# Start a trace
trace = tf.profiler.experimental.start(service_addr='localhost:6009')

# Define your computation graph here
# ...

# Stop the trace and write it into a file
with tf.profiler.experimental.Trace('train', step_num=1000, _r=1):
  pass

trace.stop()
