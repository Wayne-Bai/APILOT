
import tensorflow as tf

# Start the trace
tf.profiler.start('./logdir')

# Train your model here

# Stop the trace
tf.profiler.stop()

# Export the trace as a Summary
tf.profiler.export_to_profiler(
    tf.profiler.Profile('./logdir'),
    'trace_name',
    profile_dir('./logdir')
)

# Export the trace as a profile file
tf.profiler.export_to_tensorboard(
    tf.profiler.Profile('./logdir'),
    './logdir'
)
