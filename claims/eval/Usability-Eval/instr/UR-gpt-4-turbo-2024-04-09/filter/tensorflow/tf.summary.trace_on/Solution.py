import tensorflow as tf

# Create a TensorFlow function to trace
@tf.function
def my_function(x):
    return x * x

# Set up TensorFlow profiling
tf.profiler.experimental.start('logdir')

# Execute the function
result = my_function(tf.constant(5.0))

# Stop the profiler
tf.profiler.experimental.stop()

print("Result of my function: ", result)
