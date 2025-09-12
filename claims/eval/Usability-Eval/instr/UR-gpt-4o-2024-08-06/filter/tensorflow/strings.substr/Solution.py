import tensorflow as tf

# Define a Tensor of strings
string_tensor = tf.constant(["Hello, World!", "TensorFlow", "Python"])

# Define start positions and lengths for substrings
start_positions = tf.constant([0, 0, 0])
lengths = tf.constant([5, 6, 6])

# Use tf.strings.substr to extract substrings
substrings = tf.strings.substr(string_tensor, start_positions, lengths)

# Execute the operation in a TensorFlow session (eager execution context)
tf.print("Substrings:", substrings)
