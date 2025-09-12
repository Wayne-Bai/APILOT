import tensorflow as tf

# Create a TensorFlow function to demonstrate tracing
@tf.function
def my_function(x):
    return x * tf.math.sin(x)

# Create a summary writer for exporting the profile
logdir = "logs/profile"
summary_writer = tf.summary.create_file_writer(logdir)

# Start tracing for the function
tf.profiler.experimental.start(logdir)

# Execute the function with some sample input
for i in range(100):
    my_function(tf.constant(i, dtype=tf.float32))

# Stop tracing and export the results
tf.profiler.experimental.stop()
