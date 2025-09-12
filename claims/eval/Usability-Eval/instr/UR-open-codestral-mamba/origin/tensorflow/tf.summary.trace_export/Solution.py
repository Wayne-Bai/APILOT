import tensorflow as tf

# Initialize a summary writer object.
summary_writer = tf.summary.create_file_writer('path_to_your_log_directory')

# Inside a function where you have made some computations:
def compute_and_log_something():
    with summary_writer.as_default():
        # Let's say you have calculated some variable in your computation
        calculated_var = tf.constant(12.3)

        # Now you can log this variable and visible in TensorBoard
        tf.summary.scalar('My Calculated Variable', calculated_var)

# After your computations, stop and export the active trace as a Summary and/or Profile file.
summary_writer.close()
