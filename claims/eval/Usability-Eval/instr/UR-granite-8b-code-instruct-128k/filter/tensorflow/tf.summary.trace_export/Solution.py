import tensorflow as tf

# Start a trace
tf.summary.trace_on()

# Run the model
run_model()

# Stop the trace
tf.summary.trace_export(name="my_trace", step=0)
