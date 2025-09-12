import tensorflow as tf

# A sample function that computes the sum of two numbers
@tf.function
def compute_sum(a, b):
    with tf.summary.trace_on():
        result = tf.add(a, b)
        # Make sure to convert to int or float for visualization
        tf.summary.trace_export(
            name="sum_trace",
            step=0,
            profiler_outdir="/tmp/logs"
        )
    return result

# Call the function
compute_sum(tf.constant(1.0), tf.constant(2.0))
