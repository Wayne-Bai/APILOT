import tensorflow as tf
from datetime import datetime

# Define a summary_writer to write the logs.
logdir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
summary_writer = tf.summary.create_file_writer(logdir)

# Let's assume we have a TensorFlow operation
a = tf.constant(5, name='a')
b = tf.constant(3, name='b')
c = tf.add(a, b)

# Log the operation using summary writer
with summary_writer.as_default():
    tf.summary.trace_on(graph=True, profiler=True)
    c_value = c.numpy()
    tf.summary.trace_export('my_tf_function_trace', step=0, profiler_outdir=logdir)

# Close the summary_writer
summary_writer.close()
