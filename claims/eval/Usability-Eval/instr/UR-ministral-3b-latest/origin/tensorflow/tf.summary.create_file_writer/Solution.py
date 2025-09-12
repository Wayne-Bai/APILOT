import tensorflow as tf

# Set the log directory
log_dir = './logs'

# Create a summary file writer
file_writer = tf.summary.create_file_writer(log_dir)

# Open the file writer
with file_writer.as_default():
    print("File writer created and opened.")

# Close the file writer (optional, file writer automatically closed when context manager exits)
