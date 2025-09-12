
import tensorflow as tf

# Define a function to create and export trace
def export_active_trace(output_dir):
    # Set up the TensorFlow profiler for tracing
    tf.profiler.experimental.start(output_dir)

    # Your TensorFlow code here (e.g., model training or evaluation)

    # Stop the profiler and export the trace
    tf.profiler.experimental.stop()

# Example of using the function
output_directory = './logs'
export_active_trace(output_directory)
