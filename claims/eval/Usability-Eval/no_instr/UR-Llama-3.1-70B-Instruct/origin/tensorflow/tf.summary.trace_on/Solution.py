import tensorflow as tf

# Create a context to trace
with tf.profiler.Profiler(tf.Graph()) as p:
  # Call the operation(s) that you want to trace
  x = tf.constant([1, 2, 3])
  y = tf.constant([4, 5, 6])
  result = tf.add(x, y)
  
  # Run the operation and generate trace
  tf.print(result)

# Save the profile trace to a file
p.export_chrome_trace('trace.json')

# Alternatively, you can use the `tf.profiler.experimental.Profiler` 
# which is the recommended profiler API.

# Create a profiler
tf.profiler.experimental.Profiler_options(
    tf.profiler.ProfilerOptions(
        host_tracer_level=2,  # 0:No tracing, 1: Model only, 2: Model and embedding, 3: Full tracing
        python_tracer_level=1  # 0: Not enabled, 1: Memory, 2: Memory and CPU
    )
)

with tf.profiler.experimental.Profiler():  
  # Call the operation(s) that you want to trace
  x = tf.constant([1, 2, 3])
  y = tf.constant([4, 5, 6])
  result = tf.add(x, y)
  tf.print(result)
