import tensorflow as tf

# Start a trace to record computation graphs and profiling information
with tf.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    run_metadata = tf.RunMetadata()
    sess.run(your_op, options=tf.compat.v1.RunOptions(trace_level=tf.RunOptions.FULL_TRACE),
             run_metadata=run_metadata)
