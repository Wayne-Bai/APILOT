
import tensorflow as tf

# Start the TensorFlow profiler and trace exporter
profiler = tf.profiler.experimental.start()
trace_exporter = tf.profiler.experimental.TraceExporter(profiler)

# Set up a SummaryWriter to export summaries
summary_writer = tf.summary.create_file_writer('./summaries')

# Export the active trace as a Summary and/or profile file
trace_exporter.export_trace()
