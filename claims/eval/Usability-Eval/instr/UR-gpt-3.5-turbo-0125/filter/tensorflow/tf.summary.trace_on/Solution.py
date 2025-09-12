
import tensorflow as tf

# Start a trace to record computation graphs and profiling information
with tf.Graph().as_default(), tf.compat.v1.Session() as sess:
    run_options = tf.compat.v1.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
    run_metadata = tf.compat.v1.RunMetadata()

    # Run your TensorFlow operations here

    # Get the profiling information
    results = sess.run(fetches=[...], options=run_options, run_metadata=run_metadata)

    # Code to analyze the trace and profiling information
