import tensorflow as tf

# Enable eager execution to start a trace to record computation graphs and profiling information.
tf.compat.v1.enable_eager_execution()

# Start recording
tf.compat.v1.profiler.start()

# Your computation or model training code goes here
# e.g., A simple matrix multiplication
a = tf.constant([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0]])
b = tf.constant([[7.0, 8.0],
                 [9.0, 10.0],
                 [11.0, 12.0]])
c = tf.matmul(a, b)

# Print the result
print(c)

# Stop recording
tf.compat.v1.profiler.stop()
