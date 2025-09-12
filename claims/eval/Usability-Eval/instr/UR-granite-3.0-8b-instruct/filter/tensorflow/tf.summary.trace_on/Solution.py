import tensorflow as tf

# Start tracing
runner = tf.contrib.tfprof.trace.TraceRunner(tf.contrib.tfprof.trace.TraceOptions())

# Run your model or computations here
# For example:
# model = your_model()
# runner.add_step(model)

# Stop tracing and print the results
runner.start()
# Run your model or computations here
# For example:
# model = your_model()
# runner.add_step(model)
runner.stop()

# Print the results
runner.print_results()
