import tensorflow as tf

# Start a trace to record computation graphs and profiling information
tf.profiler.experimental.start('logdir')

# Example computation to trace
@tf.function
def example_computation(x):
    return x ** 2

# Run the example computation
result = example_computation(tf.constant(3.0))

# Stop the trace
tf.profiler.experimental.stop()

print("Result of computation:", result.numpy())
