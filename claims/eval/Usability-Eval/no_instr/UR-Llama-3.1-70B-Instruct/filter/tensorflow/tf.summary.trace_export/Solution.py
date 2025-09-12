import tensorflow as tf

# Create a TensorFlow session
sess = tf.Session()

# Start tracing
tf.RunOptions()
tf.RunMetadata()
options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
run_metadata = tf.RunMetadata()

# Create a simple TensorFlow graph
a = tf.constant(1, name="a")
b = tf.constant(2, name="b")
c = tf.add(a, b, name="addition")

# Run the graph and capture the metadata
sess.run(c, options=options, run_metadata=run_metadata)

# Export the trace as a Summary
from tensorflow.python.framework import summary
summary_str = summary.summarize_run_metadata(run_metadata)
writer = tf.summary.FileWriter('summaries')
writer.add_summary(summary_str)
writer.close()

# Export the trace as a profile file
from tensorflow.python.profiler import model_analyzer
profiler = model_analyzer.Profiler(graph=sess.graph)
profiler.add_step(step=0, run_metadata=run_metadata)
profiler.profile_name(scope="profile")

# Stop tracing
sess.close()
