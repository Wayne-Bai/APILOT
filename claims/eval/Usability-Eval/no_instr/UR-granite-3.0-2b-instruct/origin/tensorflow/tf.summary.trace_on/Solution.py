import tensorflow as tf

# Create a computational graph
add = tf.add(x, y)
sub = tf.subtract(x, y)

# Start a trace to record computation graphs and profiling information
tf.profiler.start("my_profile")

# Run the computational graph
with tf.Session() as sess:
    result_add = sess.run(add)
    result_sub = sess.run(sub)

# Stop the trace
tf.profiler.stop("my_profile")
